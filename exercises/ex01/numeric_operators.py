"""EX01 practicing numeric operators and type conversions"""

__author__: str = "730224009"

left_side: int = int(input("Left-hand side: "))
right_side: int = int(input("Right-hand side: "))

print(str(left_side) + " ** " + str(right_side) + " is " + str(left_side**right_side))
print(str(left_side) + " / " + str(right_side) + " is " + str(left_side/right_side))
print(str(left_side) + " // " + str(right_side) + " is " + str(left_side//right_side))
print(str(left_side) + " % " + str(right_side) + " is " + str(left_side%right_side))
