from Environment import Environment
from Controller import Controller

environment = Environment()
controller = Controller(environment)
controller.start_animate_loop()
