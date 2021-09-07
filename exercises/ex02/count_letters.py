"""Counting letters in a string."""

__author__ = "730224009"


# Begin your solution here...
given_letter: str = input("What letter do you want to search for?: ")
given_word: str = input("Enter a word: ")
counter: int = 0
output_number: int = 0

while counter < len(given_word):
    if given_word[counter] == given_letter:
        output_number = output_number + 1
        counter = counter + 1
    else:
        counter = counter + 1

print("Count: " + str(output_number))