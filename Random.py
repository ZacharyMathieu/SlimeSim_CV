import random


def get_random_int() -> int:
    return random.randint()


def get_random_float() -> float:
    return random.random()


def get_random_bool(true_odds: float) -> bool:
    return get_random_float() < true_odds
