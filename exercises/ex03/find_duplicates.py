"""Finding duplicate letters in a word."""

__author__ = "730224009"

given_word: str = input("Enter a word: ")
counter: int = 0
counter2: int = 0
length: int = len(given_word)
length2: int = len(given_word)

while counter + 1 < length:  # comparing neighbors
    if given_word[counter] != given_word[counter + 1]:
        counter = counter + 1
    else:
        length = -1
        length2 = -1
        print("Found duplicate: True")

while counter2 < length2:  # comparing to each
    letter_counter: int = counter2 + 2
    while letter_counter < length2:
        if given_word[counter2] != given_word[letter_counter]:
            letter_counter = letter_counter + 1
        else:
            length2 = -1
            print("Found duplicate: True")
    counter2 = counter2 + 1


if length and length2 > 0:
    print("Found duplicate: False")