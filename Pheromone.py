from EnvironmentData import EnvironmentData
import Constants
import Optim


class Pheromone:
    __level: float = 0
    __active: bool = True
    __need_highlight: bool = False
    __slime_id: int
    __env_data: EnvironmentData
    __x: int
    __y: int

    def __init__(self, data: EnvironmentData, x: int, y: int):
        self.__env_data = data
        self.__slime_id = None
        self.__x = x
        self.__y = y

    def add_slime_level(self) -> None:
        if self.__active:
            self.__level += self.__env_data.slime_pheromone_level
            if self.__level > self.__env_data.pheromone_max_level:
                self.__level = self.__env_data.pheromone_max_level

    def diffuse(self) -> None:
        if self.__env_data.pheromone_max_level < self.__level:
            self.__level = Constants.PHEROMONE_MAX_LEVEL_RESET_VALUE

        self.__level -= (self.__env_data.pheromone_low_level_diffusion_multiplier *
                         (1 - (self.__level / self.__env_data.pheromone_max_level)))

        self.__level -= (self.__env_data.pheromone_high_level_diffusion_multiplier *
                         (self.__level / self.__env_data.pheromone_max_level))

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

    def get_level(self) -> float:
        return self.__level

    def get_slime_id(self) -> int:
        return self.__slime_id

    def set_slime_id(self, p_id: int) -> None:
        self.__slime_id = p_id

    def get_active(self) -> bool:
        return self.__active

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y
