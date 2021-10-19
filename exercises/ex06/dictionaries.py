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
            key = a[key] 
            new_dict[key] = key

    return new_dict