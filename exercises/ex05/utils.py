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


def sub(c: list[int], start_index: int, end_index: int) -> list[int]:
    new_list: list[int] = list()
    counter: int = 0
    # finder: int = start_index
    while counter < len(c) and start_index < len(c) and end_index > 0:
        if start_index >= 0:
            finder: int = start_index
        else:
            finder: int = 0
        
        if end_index <= len(c):
            stopper: int = end_index
        else:
            stopper: int = len(c)

        while finder < stopper:
            new_list.append(c[finder])
            finder += 1
        counter = len(c)

    return new_list

