"""Creating an adventure with functions and procedures."""

__author__ = "730224009"

## variable naming
player: str = ""


def main() -> None:
    """Enters adventure and establishes home base."""
    greet()
    homebase()
    

def greet() -> None:
    """Greets the player and establishes name."""
    print("Welcome to Adventure Island!")
    player = input("What is your name? ")
    print(f"Greetings, {player}! \nLegend has it, long ago, dread Pirate Blackbeard sailed here with his crew to hide his most valuable treasure-- the Crown of Emeralds. \nFor the past two centuries, adventurers like yourself have scoured this island to no avail...")


def homebase() -> None:
    print("You have adventure points.") ## add f string
    print("How would you like to proceed?")
    print("1: I want to search the beaches. \n2: I want to search the jungle. \n3: I want to leave Adventure Island.")
    choice: int = int(input("Enter the number of your action: "))
    if choice == 1 or choice == 2:
        if choice == 1:
            beach()
        else:
            jungle()
    else:
        print(f"You have chosen to leave Adventure Island. You have adventure points. Good luck next time, {player}!")



if __name__ == "__main__":
    main()