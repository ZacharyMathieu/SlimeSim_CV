from EnvironmentData import EnvironmentData
import Constants


class Pheromone:
    __level: float = 0
    __active: bool = True
    __need_highlight: bool = False
    __slime_id: int
    __env_data: EnvironmentData

    def __init__(self, data: EnvironmentData):
        self.__env_data = data

    def add_slime_level(self) -> None:
        if self.__active:
            self.__level += self.__env_data.slime_pheromone_level
            if self.__level > self.__env_data.pheromone_max_level:
                self.__level = self.__env_data.pheromone_max_level

    def diffuse(self) -> None:
        if self.__active and self.__level > 0:
            if self.__env_data.pheromone_max_level < self.__level:
                self.__level = Constants.PHEROMONE_MAX_LEVEL_RESET_VALUE

            self.__level -= self.__env_data.pheromone_low_level_diffusion_multiplier * (
                    (1 / (self.__level + 1)) - (1 / (self.__env_data.pheromone_low_level_diffusion_multiplier + 1)))
            self.__level -= (self.__env_data.pheromone_high_level_diffusion_multiplier * (
                    self.__level / self.__env_data.pheromone_max_level)) / self.__env_data.pheromone_max_level
            self.__level -= self.__env_data.pheromone_diffusion_constant

            if self.__level < 0:
                self.__level = 0

    def highlight(self) -> None:
        self.__need_highlight = True

    def lowlight(self) -> bool:
        if self.__need_highlight:
            self.__need_highlight = False
            return True
        return False

    def deactivate(self) -> None:
        self.__active = False
