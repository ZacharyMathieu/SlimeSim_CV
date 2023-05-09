import numpy as np

import Random
from EnvironmentData import EnvironmentData


class PheromoneGrid:
    __env_data: EnvironmentData
    __grid: np.ndarray

    def __init__(self, width: int, height: int, data: EnvironmentData):
        self.__env_data = data

        self.update_size()

        for i in range(self.__env_data.random_natural_pheromones_count):
            x = int(Random.get_random_float() * width)
            y = int(Random.get_random_float() * height)

            self.__grid[x,y].deactivate()
            self.__grid[x,y].level = self.__env_data.natural_pheromones_strength

    def update(self) -> None:
        self.__grid.ma
        for (std.vector < Pheromone * > & line: * grid) :
            for (Pheromone * pheromone: line) :
                pheromone.diffuse()

    void
    PheromoneGrid.addSlimeLevel(int
    x, int
    y) {
        grid.at(y).at(x).addSlimeLevel()
    }

    void
    PheromoneGrid.setSlimeId(int
    x, int
    y, long
    id) {
        grid.at(y).at(x).slimeId = id
    }

    std.vector < std.vector < Pheromone * >>
    *PheromoneGrid.getGrid()
    {
    return grid
    }

    void
    PheromoneGrid.updateSize()
    {
    grid = new
    std.vector < std.vector < Pheromone * >> ()

    for (int y = 0 y < envData.grid_height y++) {
        std.vector < Pheromone * > v = std.vector < Pheromone * > ()

    for (int x = 0 x < envData.grid_width x++) {
    v.push_back(new Pheromone(envData))
    }
    grid.push_back(v)
    }

}
