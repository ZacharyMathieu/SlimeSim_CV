from collections.abc import Iterator

from Slime import Slime


class SlimeVector:
    __slime_list: list[Slime]

    def __init__(self):
        self.__slime_list = []

    def __iter__(self) -> Iterator[Slime]:
        return iter(self.__slime_list)

    def __len__(self) -> int:
        return len(self.__slime_list)

    def append(self, slime: Slime) -> None:
        self.__slime_list.append(slime)
