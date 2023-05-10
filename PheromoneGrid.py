import numpy as np

import Random
from EnvironmentData import EnvironmentData
from Pheromone import Pheromone


def d(p: Pheromone) -> None:
    if p is not None:
        p.diffuse()


class PheromoneGrid:
    __env_data: EnvironmentData
    __grid: np.ndarray

    def __init__(self, width: int, height: int, data: EnvironmentData):
        self.__env_data = data

        self.update_size()

        for i in range(self.__env_data.random_natural_pheromones_count):
            x = int(Random.get_random_float() * width)
            y = int(Random.get_random_float() * height)

            self.__grid[x, y].deactivate()
            self.__grid[x, y].level = self.__env_data.natural_pheromones_strength

    diffuse_vectorized = np.vectorize(d)

    # TODO: Does this realy work???
    def update(self) -> None:
        self.diffuse_vectorized(self.__grid)

    def add_slime_level(self, x: int, y: int) -> None:
        self.__grid[x, y].add_slime_level()

    def set_slime_id(self, x: int, y: int, p_id: int) -> None:
        self.__grid[x, y].set_slime_id(p_id)

    def get_grid(self) -> np.ndarray:
        return self.__grid

    def update_size(self) -> None:
        self.__grid = np.ndarray((self.__env_data.grid_width, self.__env_data.grid_width), Pheromone)

        for x in range(self.__env_data.grid_width):
            for y in range(self.__env_data.grid_height):
                self.__grid[x, y] = Pheromone(self.__env_data)
