"""Creating an adventure with functions and procedures."""

__author__ = "730224009"

## variable naming
player: str = ""


def main() -> None:
    """Enters adventure."""
    global points
    global player
    player = "name"
    points = 0

    greet()

    #  game loop
    choice: int = 1
    while choice >= 0:
        if choice == 0:  ## 0 = exit game
            #  make all this exit_game()
            print("You have chosen to leave Adventure Island.")
            print(f"You have {points} adventure points.")
            print(f"Good luck next time, {player}!")
            choice = -1

        if choice == 1:  ##  1 = home base
            #  make all this home_base()
            print(f"You have {points} adventure points.")
            print("How do you want to proceed?")
            print("2: I want to search the beaches. \n3: I want to search the jungle. \n0: I want to leave Adventure Island.")
            choice = int(input("Enter the number of your action: "))
            points = add_points(points)

        if choice == 2:  ## 2 = search beaches
            #  make all this search_beaches()
            print(f"You have {points} adventure points.")
            print(f"Congratulations, {player}! You found the Emerald Crown!")
            choice = int(input("Enter the number of your action: "))
            points = treasure_points(points)

        if choice == 3:  ##  3 = search jungle
            #  make all this search_jungle()
            print(f"You have {points} adventure points.")
            print("jungle")
            choice = -1
            points = add_points(points)
    

def greet() -> None:
    """Greets the player and establishes name."""
    global player
    print("Welcome to Adventure Island!")
    player = input("What is your name? ")
    print(f"Greetings, {player}! \nLegend has it, long ago, dread Pirate Roberts sailed here with his crew to hide his most valuable treasure-- the Crown of Emeralds. \nFor the past two centuries, adventurers like yourself have scoured this island to no avail...")


def add_points(a: int) -> int:
    a = 10 + a
    return a


def treasure_points(a: int) -> int: 
    a = 1000 + a
    return a


def subtract_points(a: int) -> int:
    a = a - 5
    return a

    
if __name__ == "__main__":
    main()