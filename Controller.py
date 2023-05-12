import numpy as np
import threading
import time
import cv2

from Environment import Environment
from EnvironmentDisplay import EnvironmentDisplay
import Constants
import Optim


class Controller:
    __environment: Environment
    __canvas: np.ndarray
    __animate_loop_active: bool = False
    __parameters_loop_active: bool = False
    __wait_for_animate = False
    __waiting_for_animate = False

    def __init__(self, canvas: np.ndarray = None):
        self.__environment = Environment()
        if canvas is not None:
            self.__canvas = canvas
        else:
            self.__canvas = np.zeros(
                (self.__environment.get_height(), self.__environment.get_width(), Constants.WINDOW_COLOR_CHANNELS))

    def physics(self) -> None:
        self.__environment.physics()

    def animate(self) -> bool:
        self.__waiting_for_animate = self.__wait_for_animate
        while self.__wait_for_animate:
            time.sleep(0)
        self.__waiting_for_animate = self.__wait_for_animate

        self.physics()

        return EnvironmentDisplay.display_environment(self.__environment, self.__canvas)

    def animate_loop(self) -> None:
        while self.__animate_loop_active:
            if self.animate():
                time.sleep(Constants.CANVAS_REFRESH_PERIOD_MS / 1000)
            else:
                self.__animate_loop_active = False
                self.__parameters_loop_active = False
                cv2.destroyAllWindows()
            # print("frame")

    def start_animate_loop(self) -> None:
        self.__animate_loop_active = True
        self.animate_loop()

    def stop_animate_loop(self) -> None:
        self.__animate_loop_active = False

    def update_parameters(self) -> None:
        self.__wait_for_animate = True
        while not self.__waiting_for_animate:
            time.sleep(0.1)

        self.__environment.update_parameters()
        shape_env = (self.__environment.get_height(), self.__environment.get_width(), Constants.WINDOW_COLOR_CHANNELS)
        shape_canvas = self.__canvas.shape
        if shape_env != shape_canvas:
            self.__canvas = np.zeros(
                (self.__environment.get_height(), self.__environment.get_width(), Constants.WINDOW_COLOR_CHANNELS))

        self.__wait_for_animate = False

    def parameters_loop(self) -> None:
        while self.__parameters_loop_active:
            self.update_parameters()
            time.sleep(Constants.PARAMETER_UPDATE_PERIOD_MS / 1000)

    def start_parameter_update_thread(self) -> None:
        self.__parameters_loop_active = True
        threading.Thread(target=self.parameters_loop).start()

    def stop_parameter_update_thread(self) -> None:
        self.__parameters_loop_active = False
