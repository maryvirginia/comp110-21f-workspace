"""Practice with dictionaries."""

__author__ = "730224009"

# Define your functions below


def invert(a: dict[str, str]) -> dict[str, str]:
    """Swaps keys and values."""
    new_dict: dict[str, str] = {}
    for key in a:
        does_new_key_exist: bool = a[key] in new_dict
        if does_new_key_exist == True:
            # raise key error
            raise KeyError("KeyError: new key already exists.")
        else:
            # proceed with adding key and value to new_dict
            new_value: str = a[key]
            new_dict[new_value] = key

    return new_dict


def favorite_color(b: dict[str, str]) -> str:
    """Returns most popular favorite color from a given dict."""
    tracker_dict: dict[str, int] = {}
    for key in b:
        tracker_key: str = b[key]
        if b[key] in tracker_dict:
            tracker_dict[tracker_key] += 1
        else:
            tracker_dict[tracker_key] = 0

    current_max: int = 0
    for key in tracker_dict:
        if tracker_dict[key] > current_max:
            current_max = tracker_dict[key]

    for key in tracker_dict:
        if current_max == tracker_dict[key]:
            return key 


def count(c: list[str]) -> dict[str, int]:
    """Returns dict with frequencies of items in a list."""
    new_dict: dict[str, int] = {}
    for item in c:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    
    return new_dict 