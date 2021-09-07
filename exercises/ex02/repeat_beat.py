"""Repeating a beat in a loop."""

__author__ = "730224009"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
given_number: int = int(input("How many times do you want to repeat it? "))

total_beat: str = (beat)
counter: int = 0

while given_number > (counter + 1):
    total_beat = total_beat + " " + beat
    counter = counter + 1

if given_number <= 0:
    print("No beat...")
else:
    print(total_beat)