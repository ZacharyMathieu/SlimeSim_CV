import numpy as np
import cv2

from Environment import Environment
from Pheromone import Pheromone
import Constants
import Optim


class EnvironmentDisplay:
    @staticmethod
    def display_environment(env: Environment, canvas: np.ndarray) -> bool:
        cv2.rectangle(canvas, (0, 0), (env.get_width(), env.get_height()), (0, 0, 0), -1)

        env_data = env.get_env_data()
        grid = env.get_pheromone_grid().get_grid()

        if env_data.display_pheromones:
            for p_a in grid:
                for pheromone in p_a:
                    level = max(pheromone.get_level() / env_data.pheromone_max_level, 0.0)

                    if level > 0:
                        if pheromone.lowlight():
                            canvas[pheromone.get_y(), pheromone.get_x()] = \
                                Constants.COLOR_FROM_ARRAY(env_data.display_highlight_pheromone_color)
                        elif not pheromone.get_active():
                            canvas[pheromone.get_y(), pheromone.get_x()] = \
                                Constants.COLOR_FROM_ARRAY(env_data.display_inactive_pheromone_color)
                        else:
                            canvas[pheromone.get_y(), pheromone.get_x()] = \
                                Constants.DISPLAY_DEFAULT_PHEROMONE_COLOR(level)

        if env_data.display_slime:
            for slime in env.get_slime_vector():
                canvas[int(slime.get_y()), int(slime.get_x())] = \
                    Constants.COLOR_FROM_ARRAY(env_data.display_slime_color)

        cv2.imshow("canvas", cv2.resize(canvas, (Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT),
                                        interpolation=cv2.INTER_LINEAR))
        # cv2.imshow("canvas", canvas)
        key = cv2.waitKey(1)
        return key != 27  # escape key
