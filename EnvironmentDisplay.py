import numpy as np
import cv2

from Environment import Environment
import Constants
import Optim


class EnvironmentDisplay:
    @staticmethod
    def display_environment(env: Environment, canvas: np.ndarray) -> bool:
        def background_f():
            cv2.rectangle(canvas, (0, 0), (env.get_width(), env.get_height()), (0, 0, 0), -1)

        env_data = env.get_env_data()
        grid = env.get_pheromone_grid()

        def pheromones_f():
            if env_data.display_pheromones:
                for p_a in grid:
                    for pheromone in p_a:
                        level = max(pheromone.get_level() / env_data.pheromone_max_level, 0.0)

                        if level > 0:
                            color: tuple[int, int, int, int]

                            if pheromone.lowlight():
                                color = Constants.COLOR_FROM_ARRAY(env_data.display_highlight_pheromone_color)
                            elif not pheromone.get_active():
                                color = Constants.COLOR_FROM_ARRAY(env_data.display_inactive_pheromone_color)
                            else:
                                color = Constants.DISPLAY_DEFAULT_PHEROMONE_COLOR(level)

                            canvas[pheromone.get_y(), pheromone.get_x()] = color

        def slimes_f():
            if env_data.display_slime:
                for slime in env.get_slime_vector():
                    canvas[int(slime.get_y()), int(slime.get_x())] = \
                        Constants.COLOR_FROM_ARRAY(env_data.display_slime_color)

        def show_f():
            cv2.imshow("canvas", cv2.resize(canvas, (Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT),
                                            interpolation=cv2.INTER_LINEAR))
            key = cv2.waitKey(1)
            return key != 27  # escape key

        # Optim.time_exec("Background", background_f)
        # Optim.time_exec("Pheromones", pheromones_f)
        # Optim.time_exec("Slimes    ", slimes_f)
        # return Optim.time_exec("Show      ", show_f)
        background_f()
        pheromones_f()
        slimes_f()
        return show_f()
