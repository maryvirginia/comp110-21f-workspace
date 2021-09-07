"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730224009"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")

fortune: int = randint(1, 4)

if fortune == 1:
    print("You will face a challenge in the coming days, but your resilient spirit will prevail.")
else:
    if fortune == 2:
        print("Your life will be filled with lots of love-- be sure to share it!")
    else:
        if fortune == 3:
            print("You will meet your soulmate within the next two years!")
        else:
            if fortune == 4:
                print("Continue to treat people with kindness, and good things will be coming your way!")

print("Now, go spread positive vibes!")