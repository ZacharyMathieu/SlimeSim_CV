import numpy as np

from EnvironmentData import EnvironmentData
from PheromoneGrid import PheromoneGrid
from Slime import Slime
from InputParam import InputParam
from ParameterReader import ParameterReader
import Constants


class Environment:
    __slime_vector: np.ndarray
    __env_data: EnvironmentData
    __pheromone_grid: PheromoneGrid = None
    __seek_pheromone_timer = 0

    def __init__(self):
        self.__env_data = EnvironmentData()
        self.update_parameters()
        self.__pheromone_grid = PheromoneGrid(self.__env_data.grid_width,
                                              self.__env_data.grid_height,
                                              self.__env_data)
        self.generate_random_slime(self.__env_data.slime_count)

    def get_width(self) -> int:
        return self.__env_data.grid_width

    def get_height(self) -> int:
        return self.__env_data.grid_height

    def get_slime_count(self) -> int:
        return len(self.__slime_vector)

    def get_slime_vector(self) -> np.ndarray:
        return self.__slime_vector

    def get_pheromone_grid(self) -> PheromoneGrid:
        return self.__pheromone_grid

    def move_all_slime(self) -> None:
        seek_pheromones = False

        self.__seek_pheromone_timer += 1

        if self.__seek_pheromone_timer % self.__env_data.slime_seek_pheromones_period == 0:
            seek_pheromones = True
            self.__seek_pheromone_timer = 0

        for slime in self.__slime_vector:
            slime.move_forward(self.__pheromone_grid, self.__slime_vector, seek_pheromones)

    def update_pheromones(self) -> None:
        for slime in self.__slime_vector:
            self.__pheromone_grid.add_slime_level(int(slime.get_x()), int(slime.get_y()))
            self.__pheromone_grid.set_slime_id(int(slime.get_x()), int(slime.get_y()), slime.get_id())

        self.__pheromone_grid.update()

    def physics(self) -> None:
        self.move_all_slime()
        self.update_pheromones()

    def generate_random_slime(self, slime_count: int) -> None:
        self.__slime_vector = np.ndarray(slime_count, Slime)
        for i in range(slime_count):
            self.__slime_vector[i] = Slime.generate_random(i, self.__env_data)

    def get_info_string(self, spacing_count: int) -> str:
        spacing = " " * spacing_count

        s = spacing + "Environment info:\n" + \
            spacing + " Width: " + self.__env_data.grid_width.__str__() + "\n" + \
            spacing + " Height: " + self.__env_data.grid_height.__str__() + "\n" + \
            spacing + " Slime count: " + self.get_slime_count().__str__() + "\n" + \
            spacing + " Slime list:\n" + "\n"

        for slime in self.__slime_vector:
            s += spacing + slime.get_info_string(spacing_count + 2) + "\n"

        return s.str()

    def __update_param(self, param: InputParam) -> None:
        if param.name == "display_pheromones":
            if self.__env_data.display_pheromones != param.value_bool:
                print("display_pheromones set to : [" + param.value_bool.__str__() + "]\n")
                self.__env_data.display_pheromones = param.value_bool
        elif param.name == "display_slime":
            if self.__env_data.display_slime != param.value_bool:
                print("display_slime set to : [" + param.value_bool.__str__() + "]\n")
                self.__env_data.display_slime = param.value_bool
        elif param.name == "display_slime_size":
            if self.__env_data.display_slime_size != param.value_number:
                print("display_slime_size set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.display_slime_size = int(param.value_number)
        elif param.name == "display_slime_opacity":
            if self.__env_data.display_slime_opacity != param.value_number:
                print("display_slime_opacity set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.display_slime_opacity = int(param.value_number)
        elif param.name == "display_slime_color":
            # print("display_slime_color not yet implemented\n")
            pass
        elif param.name == "display_highlight_pheromone_color":
            # print("display_highlight_pheromone_color not yet implemented\n")
            pass
        elif param.name == "display_inactive_pheromone_color":
            # print("display_inactive_pheromone_color not yet implemented\n")
            pass
        elif param.name == "grid_width":
            if self.__env_data.grid_width != param.value_number:
                print("grid_width set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.grid_width = int(param.value_number)
                if self.__pheromone_grid is not None:
                    self.__pheromone_grid.update_size()
        elif param.name == "grid_height":
            if self.__env_data.grid_height != param.value_number:
                print("grid_height set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.grid_height = int(param.value_number)
                if self.__pheromone_grid is not None:
                    self.__pheromone_grid.update_size()
        elif param.name == "loop_grid":
            if self.__env_data.loop_grid != param.value_bool:
                print("loop_grid set to : [" + param.value_bool.__str__() + "]\n")
                self.__env_data.loop_grid = param.value_bool
        elif param.name == "random_natural_pheromones_count":
            if self.__env_data.random_natural_pheromones_count != param.value_number:
                print("random_natural_pheromones_count set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.random_natural_pheromones_count = int(param.value_number)
        elif param.name == "natural_pheromones_strength":
            if self.__env_data.natural_pheromones_strength != param.value_number:
                print("natural_pheromones_strength set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.natural_pheromones_strength = int(param.value_number)
        elif param.name == "slime_count":
            if self.__env_data.slime_count != param.value_number:
                print("slime_count set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.slime_count = int(param.value_number)
        elif param.name == "slime_speed":
            if self.__env_data.slime_speed != param.value_number:
                print("slime_speed set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.slime_speed = param.value_number
        elif param.name == "slime_avoid_walls":
            if self.__env_data.slime_avoid_walls != param.value_bool:
                print("slime_avoid_walls set to : [" + param.value_bool.__str__() + "]\n")
                self.__env_data.slime_avoid_walls = param.value_bool
        elif param.name == "slime_wall_detection_range":
            if self.__env_data.slime_wall_detection_range != param.value_number:
                print("slime_wall_detection_range set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.slime_wall_detection_range = int(param.value_number)
        elif param.name == "slime_wall_turn_angle":
            if self.__env_data.slime_wall_turn_angle != param.value_number:
                print("slime_wall_turn_angle set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.slime_wall_turn_angle = param.value_number
        elif param.name == "slime_seek_pheromones":
            if self.__env_data.slime_seek_pheromones != param.value_bool:
                print("slime_seek_pheromones set to : [" + param.value_bool.__str__() + "]\n")
                self.__env_data.slime_seek_pheromones = param.value_bool
        elif param.name == "slime_seek_pheromones_period":
            if self.__env_data.slime_seek_pheromones_period != param.value_number:
                print("slime_seek_pheromones_period set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.slime_seek_pheromones_period = int(param.value_number)
        elif param.name == "slime_pheromone_detection_range":
            if self.__env_data.slime_pheromone_detection_range != param.value_number:
                print("slime_pheromone_detection_range set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.slime_pheromone_detection_range = int(param.value_number)
        elif param.name == "slime_pheromone_turn_angle":
            if self.__env_data.slime_pheromone_turn_angle != param.value_number:
                print("slime_pheromone_turn_angle set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.slime_pheromone_turn_angle = param.value_number
        elif param.name == "slime_pheromone_level":
            if self.__env_data.slime_pheromone_level != param.value_number:
                print("slime_pheromone_level set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.slime_pheromone_level = int(param.value_number)
        elif param.name == "slime_ignore_self_pheromone":
            if self.__env_data.slime_ignore_self_pheromone != param.value_bool:
                print("slime_ignore_self_pheromone set to : [" + param.value_bool.__str__() + "]\n")
                self.__env_data.slime_ignore_self_pheromone = param.value_bool
        elif param.name == "slime_align_direction":
            if self.__env_data.slime_align_direction != param.value_bool:
                print("slime_align_direction set to : [" + param.value_bool.__str__() + "]\n")
                self.__env_data.slime_align_direction = param.value_bool
        elif param.name == "slime_other_detection_range":
            if self.__env_data.slime_other_detection_range != param.value_number:
                print("slime_other_detection_range set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.slime_other_detection_range = int(param.value_number)
        elif param.name == "slime_align_turn_angle":
            if self.__env_data.slime_align_turn_angle != param.value_number:
                print("slime_align_turn_angle set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.slime_align_turn_angle = param.value_number
        elif param.name == "slime_random_rotation_chance":
            if self.__env_data.slime_random_rotation_chance != param.value_number:
                print("slime_random_rotation_chance set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.slime_random_rotation_chance = param.value_number
        elif param.name == "slime_random_rotation_angle":
            if self.__env_data.slime_random_rotation_angle != param.value_number:
                print("slime_random_rotation_angle set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.slime_random_rotation_angle = param.value_number
        elif param.name == "slime_bias_direction":
            if self.__env_data.slime_bias_direction != param.value_bool:
                print("slime_bias_direction set to : [" + param.value_bool.__str__() + "]\n")
                self.__env_data.slime_bias_direction = param.value_bool
        elif param.name == "slime_bias_direction_x":
            if self.__env_data.slime_bias_direction_x != param.value_number:
                print("slime_bias_direction_x set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.slime_bias_direction_x = int(param.value_number)
        elif param.name == "slime_bias_direction_y":
            if self.__env_data.slime_bias_direction_y != param.value_number:
                print("slime_bias_direction_y set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.slime_bias_direction_y = int(param.value_number)
        elif param.name == "slime_bias_rotation_angle":
            if self.__env_data.slime_bias_rotation_angle != param.value_number:
                print("slime_bias_rotation_angle set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.slime_bias_rotation_angle = param.value_number
        elif param.name == "pheromone_max_level":
            if self.__env_data.pheromone_max_level != param.value_number:
                print("pheromone_max_level set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.pheromone_max_level = int(param.value_number)
        elif param.name == "pheromone_high_level_diffusion_multiplier":
            if self.__env_data.pheromone_high_level_diffusion_multiplier != param.value_number:
                print("pheromone_high_level_diffusion_multiplier set to : [" + param.value_number.__str__() + "]")
                self.__env_data.pheromone_high_level_diffusion_multiplier = param.value_number
        elif param.name == "pheromone_low_level_diffusion_multiplier":
            if self.__env_data.pheromone_low_level_diffusion_multiplier != param.value_number:
                print("pheromone_low_level_diffusion_multiplier set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.pheromone_low_level_diffusion_multiplier = int(param.value_number)
        elif param.name == "pheromone_diffusion_constant":
            if self.__env_data.pheromone_diffusion_constant != param.value_number:
                print("pheromone_diffusion_constant set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.pheromone_diffusion_constant = int(param.value_number)
        elif param.name == "pheromone_max_level_reset_value":
            if self.__env_data.pheromone_max_level_reset_value != param.value_number:
                print("pheromone_max_level_reset_value set to : [" + param.value_number.__str__() + "]\n")
                self.__env_data.pheromone_max_level_reset_value = int(param.value_number)
        else:
            print("UNRECOGNIZED PARAMETER: [" + param.name + "]\n")

    def update_parameters(self) -> None:
        param_file_name = Constants.PARAMETER_FILE_NAME
        params: list[InputParam] = ParameterReader.read(param_file_name)
        for param in params:
            self.__update_param(param)

    def get_environment_data(self) -> EnvironmentData:
        return self.__env_data
