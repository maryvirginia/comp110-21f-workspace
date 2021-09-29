"""List utility functions."""

__author__ = "730224009"


# TODO: Implement your functions here.


def all(x: list[int], z: int) -> bool:
    """Determines if all ints in a list are the same as a given int."""
    counter: int = 0
    if counter == len(x):
        return False
    else:
        while counter < len(x):
            item: int = x[counter]
            if item != z:
                return False
            else:
                counter += 1

        return True


def is_equal(a: list[int], b: list[int]) -> bool:
    """Determines if two given lists are deeply equal."""
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


def max(z: list[int]) -> int:
    """Finds the maximum value in a given list."""
    if len(z) == 0:
        raise ValueError("max() arg is an empty List")
        
    else:
        i: int = 0
        current_max: int = z[0]
        counter: int = 0
        while i < len(z):
            current_comparison: int = z[counter]
            if current_max > current_comparison:
                counter += 1
                i += 1
            else:
                current_max = current_comparison
                counter += 1
                i += 1
        return current_max
