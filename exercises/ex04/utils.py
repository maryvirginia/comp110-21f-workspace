"""List utility functions."""

__author__ = "730224009"


# TODO: Implement your functions here.


def all(x: list[int], z: int) -> bool:
    counter: int = 0
    while counter < len(x):
        item: int = x[counter]
        if item != z:
            return False
        else:
            counter += 1

    return True
