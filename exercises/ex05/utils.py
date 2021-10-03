"""List utility functions part 2."""

__author__ = "730224009"

# Define your functions below


def only_evens(a: list[int]) -> list[int]:
    index: int = 0
    item: int = a[index]
    while index < len(a):
        if item % 2 != 0:
            a.pop(a[index])
            index += 1
        else:
            index += 1
    return a



