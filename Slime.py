from __future__ import annotations
import math

import Random
from EnvironmentData import EnvironmentData
from SlimeVector import SlimeVector
from PheromoneGrid import PheromoneGrid


class Slime:
    __id: int
    __env_data: EnvironmentData
    __x: float
    __y: float
    __angle: float
    __last_slime_aligned: Slime

    def __init__(self, _id: int, data: EnvironmentData):
        self.__id = _id

        self.__env_data = data

        self.__x = 0
        self.__y = 0
        self.__angle = 0

        self.__last_slime_aligned = None

    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y

    def get_angle(self) -> float:
        return self.__angle

    def get_id(self) -> int:
        return self.__id

    @staticmethod
    def generate_random(p_id: int, data: EnvironmentData) -> Slime:
        slime = Slime(p_id, data)
        slime.set_random_values()
        return slime

    def set_random_values(self):
        self.__x = Random.get_random_float() * (self.__env_data.grid_width - 1)
        self.__y = Random.get_random_float() * (self.__env_data.grid_height - 1)
        self.__angle = Random.get_random_float() * (2 * math.pi)

    def move_forward(self, grid: PheromoneGrid, slimes: SlimeVector, seek_pheromones: bool):
        x_speed = self.__env_data.slime_speed * math.cos(self.__angle)
        y_speed = self.__env_data.slime_speed * math.sin(self.__angle)

        self.__x += x_speed
        self.__y += y_speed

        if self.__x < 0:
            if self.__env_data.loop_grid:
                self.__x += self.__env_data.grid_width
            else:
                self.__x = 0
        elif self.__x >= self.__env_data.grid_width:
            if self.__env_data.loop_grid:
                self.__x -= self.__env_data.grid_width
            else:
                self.__x = self.__env_data.grid_width - 1

        if self.__y < 0:
            if self.__env_data.loop_grid:
                self.__y += self.__env_data.grid_height
            else:
                self.__y = 0
        elif self.__y >= self.__env_data.grid_height:
            if self.__env_data.loop_grid:
                self.__y -= self.__env_data.grid_height
            else:
                self.__y = self.__env_data.grid_height - 1

        if self.__env_data.slime_avoid_walls:
            self.avoid_walls(x_speed, y_speed)

        if self.__env_data.slime_seek_pheromones:
            if seek_pheromones:
                self.seek_pheromones(grid)

        if self.__env_data.slime_align_direction:
            self.align_direction_with_nearby_slime(slimes)

        if self.__env_data.slime_bias_direction:
            self.turn_torwards(self.__env_data.slime_bias_direction_x, self.__env_data.slime_bias_direction_y,
                               self.__env_data.slime_bias_rotation_angle)

    def avoid_walls(self, x_speed: float, y_speed: float) -> bool:
        made_turn = False
        if self.__x < self.__env_data.slime_wall_detection_range:
            made_turn = True
            if y_speed >= 0:
                self.turn(False, -self.__env_data.slime_wall_turn_angle)
            else:
                self.turn(False, self.__env_data.slime_wall_turn_angle)
        elif self.__x > self.__env_data.grid_width - self.__env_data.slime_wall_detection_range:
            made_turn = True
            if y_speed >= 0:
                self.turn(False, self.__env_data.slime_wall_turn_angle)
            else:
                self.turn(False, -self.__env_data.slime_wall_turn_angle)
        elif self.__y < self.__env_data.slime_wall_detection_range:
            made_turn = True
            if x_speed >= 0:
                self.turn(False, self.__env_data.slime_wall_turn_angle)
            else:
                self.turn(False, -self.__env_data.slime_wall_turn_angle)
        elif self.__y > self.__env_data.grid_height - self.__env_data.slime_wall_detection_range:
            made_turn = True
            if x_speed >= 0:
                self.turn(False, -self.__env_data.slime_wall_turn_angle)
            else:
                self.turn(False, self.__env_data.slime_wall_turn_angle)

        return made_turn

    def seek_pheromones(self, pheromone_grid: PheromoneGrid) -> bool:
        rounded_x = round(self.__x)
        min_x = max(rounded_x - self.__env_data.slime_pheromone_detection_range, 0)
        max_x = min(rounded_x + self.__env_data.slime_pheromone_detection_range, self.__env_data.grid_width - 1)

        rounded_y = round(self.__y)
        min_y = max(rounded_y - self.__env_data.slime_pheromone_detection_range, 0)
        max_y = min(rounded_y + self.__env_data.slime_pheromone_detection_range, self.__env_data.grid_height - 1)

        if math.pi / 4 <= self.__angle < 3 * math.pi / 4:
            min_y = rounded_y
        elif 3 * math.pi / 4 <= self.__angle < 5 * math.pi / 4:
            max_x = rounded_x
        elif 5 * math.pi / 4 <= self.__angle < 7 * math.pi / 4:
            max_y = rounded_y
        else:
            min_x = rounded_x

        grid = pheromone_grid.get_grid()

        pheromone_found = False
        strongest_pheromone_pos = (0, 0)
        strongest_pheromone_distance = 0
        strongest_pheromone = 0
        for i_y in range(min_y, max_y):
            for i_x in range(min_x, max_x):
                pheromone = grid[i_x, i_y]
                if pheromone.level >= strongest_pheromone:
                    if (not self.__env_data.slime_ignore_self_pheromone) or (pheromone.slimeId != self.__id):
                        if pheromone_found and (pheromone.level == strongest_pheromone):
                            new_distance = math.sqrt(pow(i_x - self.__x, 2) + pow(i_y - self.__y, 2))

                            if strongest_pheromone_distance < new_distance:
                                strongest_pheromone_pos = (i_x, i_y)
                                strongest_pheromone_distance = new_distance
                        else:
                            pheromone_found = True
                            strongest_pheromone = pheromone.level
                            strongest_pheromone_pos = (i_x, i_y)
                            strongest_pheromone_distance = math.sqrt(
                                pow(strongest_pheromone_pos[0] - self.__x, 2) +
                                pow(strongest_pheromone_pos[1] - self.__y, 2))

            if pheromone_found and strongest_pheromone == self.__env_data.pheromone_max_level:
                break

            if pheromone_found:
                self.turn_torwards(strongest_pheromone_pos[0], strongest_pheromone_pos[1],
                                   self.__env_data.slime_pheromone_turn_angle)

        return pheromone_found

    def turn(self, can_be_random: bool, turn_angle: float) -> None:
        if can_be_random and Random.get_random_bool(self.__env_data.slime_random_rotation_chance):
            if Random.get_random_bool(0.5):
                self.__angle += self.__env_data.slime_random_rotation_chance
            else:
                self.__angle -= self.__env_data.slime_random_rotation_chance
        else:
            self.__angle += turn_angle

        if 2 * math.pi < self.__angle:
            self.__angle -= 2 * math.pi
        elif self.__angle < 0:
            self.__angle += 2 * math.pi

    def turn_to_angle(self, can_be_random: bool, target_angle: float, max_turn_angle: float) -> None:
        if target_angle < self.__angle:
            target_angle += 2 * math.pi

        if abs(target_angle - self.__angle) > abs(target_angle - (self.__angle + (2 * math.pi))):
            target_angle -= 2 * math.pi

        angle_diff = abs(self.__angle - target_angle)

        turn_angle = min(max_turn_angle, angle_diff)

        if target_angle > self.__angle:
            turn_angle = turn_angle
        else:
            turn_angle = -turn_angle

        self.turn(can_be_random, turn_angle)

    def turn_torwards(self, target_x: int, target_y: int, max_angle: float) -> None:
        floor_x = math.floor(self.__x)
        floor_y = math.floor(self.__y)

        centered_x = target_x - floor_x
        centered_y = target_y - floor_y

        target_angle = math.atan(centered_y / centered_x)

        if centered_x < 0:
            target_angle += math.pi

        if target_angle < 0:
            target_angle += 2 * math.pi

        self.turn_to_angle(True, target_angle, max_angle)

    def align_direction_with_nearby_slime(self, slimes: SlimeVector) -> bool:
        slime_found = False

        for slime in slimes:
            d_x = abs(self.__x - slime.get_x())
            d_y = abs(self.__y - slime.get_y())

            if (d_x < self.__env_data.slime_other_detection_range) and (
                    d_y < self.__env_data.slime_other_detection_range):
                if slime != self:
                    if math.sqrt((d_x * d_x) + (d_y * d_y)) <= self.__env_data.slime_other_detection_range:
                        slime_found = True
                        self.__last_slime_aligned = slime
                        self.align_direction_with_slime(slime)
                        break

        if not slime_found:
            self.__last_slime_aligned = None

        return slime_found

    def align_direction_with_slime(self, slime: Slime) -> None:
        self.turn_to_angle(True, slime.get_angle(), self.__env_data.slime_align_turn_angle)

    def get_info_string(self, spacing_count: int) -> str:
        spacing = " " * spacing_count

        s = spacing + "Slime info:\n" + \
            spacing + " self.__x: " + self.__x.__str__() + "\n" + \
            spacing + " self.__y: " + self.__y.__str__() + "\n" + \
            spacing + " self.__angle: " + self.__angle.__str__() + "\n" + \
            spacing + " Speed: " + self.__env_data.slime_speed.__str__() + "\n"

        return s
