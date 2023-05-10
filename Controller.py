import numpy as np
import threading
import time
import cv2

from Environment import Environment
from EnvironmentDisplay import EnvironmentDisplay
import Constants


class Controller:
    __environment: Environment
    __canvas: np.ndarray
    __animate_loop_active: bool = False
    __parameters_loop_active: bool = False

    def __init__(self, environment: Environment, canvas: np.ndarray = None):
        self.__environment = environment
        if canvas is not None:
            self.__canvas = canvas
        else:
            self.__canvas = np.zeros((self.__environment.get_width(), self.__environment.get_height(), 3))

    def physics(self) -> None:
        self.__environment.physics()

    def animate(self) -> bool:
        self.physics()
        return EnvironmentDisplay.displayEnvironment(self.__environment, self.__canvas)

    def animate_loop(self) -> None:
        while self.__animate_loop_active:
            if self.animate():
                time.sleep(Constants.CANVAS_REFRESH_PERIOD_MS / 1000)
            else:
                self.__animate_loop_active = False
                self.__parameters_loop_active = False
                cv2.destroyAllWindows()

    def start_animate_loop(self) -> None:
        self.__animate_loop_active = True
        self.animate_loop()

    def stop_animate_loop(self) -> None:
        self.__animate_loop_active = False

    def update_parameters(self) -> None:
        self.__environment.update_parameters()

    def parameters_loop(self) -> None:
        while self.__parameters_loop_active:
            self.update_parameters()
            time.sleep(Constants.PARAMETER_UPDATE_PERIOD_MS / 1000)

    def start_parameter_update_thread(self) -> None:
        self.__parameters_loop_active = True
        threading.Thread(target=self.parameters_loop).start()

    def stop_parameter_update_thread(self) -> None:
        self.__parameters_loop_active = False
