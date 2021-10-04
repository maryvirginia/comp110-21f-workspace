"""List utility functions part 2."""

__author__ = "730224009"

# Define your functions below


def only_evens(a: list[int]) -> list[int]:
    counter = 0
    index: int = len(a) - 1
    item: int = a[index]
    while counter < len(a):
        print("hi")
        if item % 2 != 0 or abs(item) == 1:
            a.pop()
            index -= 1
            counter += 1
        else:
            index -= 1
            counter += 1
    return a



