"""Practice with dictionaries."""

__author__ = "730224009"

# Define your functions below


def invert(a: dict[str, str]) -> dict[str, str]:
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
    tracker_dict: dict[str, int] = {}
    for key in b:
        does_color_exist: bool = b[key] in tracker_dict
        tracker_key: str = b[key]
        if does_color_exist == True:
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


