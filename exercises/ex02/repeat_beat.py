"""Repeating a beat in a loop."""

__author__ = "730224009"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
given_number: int = int(input("How many times do you want to repeat it? "))

total_beat: str = (beat)
counter: int = 0

while counter < given_number:
    if given_number > 0:
        total_beat = (beat + " ") * (given_number - 1) + beat
        print(total_beat)
        counter = counter + given_number
    else:
        print("No beat...")
        counter = counter + given_number