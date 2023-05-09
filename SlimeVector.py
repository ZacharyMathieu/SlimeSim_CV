import numpy as np

class SlimeVector:
    __slime_list: list[Slime]

    def SlimeVector(self):
        self.__slime_list = []

    def __iter__(self):
        return iter(self.__slime_list)

    def append(self, slime: Slime) -> None:
        self.__slime_list.append(slime)
