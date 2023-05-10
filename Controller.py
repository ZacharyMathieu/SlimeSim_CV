import numpy as np

from Environment import Environment
from EnvironmentDisplay import EnvironmentDisplay


class Controller:
    __environment: Environment
    __canvas: np.ndarray

    def __init__(self, environment: Environment, canvas: np.ndarray = None):
        self.__environment = environment
        if canvas is not None:
            self.__canvas = canvas
        else:
            self.__canvas = np.zeros((self.__environment.get_width(), self.__environment.get_height(), 3))

    def physics(self) -> None:
        self.__environment.physics()

    def animate(self) -> None:
        self.physics()
        EnvironmentDisplay.displayEnvironment(self.__environment, self.__canvas)

    def update_parameters(self) -> None:
        self.__environment.update_parameters()

    def get_canvas(self) -> np.ndarray:
        return self.__canvas
