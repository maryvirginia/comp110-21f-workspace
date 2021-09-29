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


def is_equal(a: list[int], b: list[int]) -> bool:
    counter_a: int = 0
    counter_b: int = 0
    if len(a) == len(b):
        while counter_a < len(a):
            item_a: int = a[counter_a]
            item_b: int = b[counter_b]
            if item_a == item_b:
                counter_a += 1
                counter_b += 1
            else:
                return False
        return True
    else:
        return False