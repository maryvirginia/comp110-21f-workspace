"""Drawing forests in a loop."""

__author__ = "730224009"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

given_depth: int = int(input("Depth: "))
counter: int = 1

while given_depth > 0:
    print(TREE * counter)
    counter = counter + 1
    given_depth = given_depth - 1