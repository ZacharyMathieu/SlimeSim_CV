import numpy as np
import cv2

from Environment import Environment


class EnvironmentDisplay:
    @staticmethod
    def displayEnvironment(env: Environment, canvas: np.ndarray) -> bool:
        # TODO
        cv2.imshow("canvas", canvas)
        key = cv2.waitKey(1)
        return key != "27"  # escape key
