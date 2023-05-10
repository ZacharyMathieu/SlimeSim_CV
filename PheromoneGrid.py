import numpy as np
from collections.abc import Iterator

import Random
from EnvironmentData import EnvironmentData
from Pheromone import Pheromone
import Optim


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

    def __getitem__(self, pos: tuple[int, int]) -> Pheromone:
        return self.__grid[pos]

    def __iter__(self) -> Iterator[Pheromone]:
        return self.__grid.__iter__()

    def update(self) -> None:
        for p_a in self.__grid:
            for p in p_a:
                if p.get_active() and p.get_level() > 0:
                    p.diffuse()
                    # Optim.bank_exec("Diffuse", p.diffuse)
        # print(Optim.time_bank)
        # Optim.reset_bank()

    def add_slime_level(self, x: int, y: int) -> None:
        self.__grid[x, y].add_slime_level()

    def set_slime_id(self, x: int, y: int, p_id: int) -> None:
        self.__grid[x, y].set_slime_id(p_id)

    def get_grid(self) -> np.ndarray:
        return self.__grid

    def update_size(self) -> None:
        self.__grid = np.ndarray((self.__env_data.grid_width, self.__env_data.grid_height), Pheromone)

        for x in range(self.__env_data.grid_width):
            for y in range(self.__env_data.grid_height):
                self.__grid[x, y] = Pheromone(self.__env_data, x, y)
