"""List utility functions part 2."""

__author__ = "730224009"

# Define your functions below


def only_evens(a: list[int]) -> list[int]:
    counter: int = 0
    b: list[int] = list()
    while counter < len(a):
        if a[counter] % 2 == 0 and a[counter] != 0:
            b.append(a[counter])
            counter += 1
        else:
            counter += 1
    return b


