"""An exercise in remainders and boolean logic."""

__author__ = "730224009"


# Begin your solution here...
given_int: int = int(input("Enter an int: "))

if given_int % 7 == 0:
    if given_int % 2 == 0:
        print("TAR HEELS")
    else:
        print("HEELS")
else:
    if given_int % 2 == 0:
        print("TAR")
    else:
        print("CAROLINA")