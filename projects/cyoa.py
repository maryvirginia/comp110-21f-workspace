"""Creating an adventure with functions and procedures."""

__author__ = "730224009"

# variable naming
player: str = ""
points: int = 0
choice: int = 0
ISLAND: str = "\U0001F3DD"


def main() -> None:
    """Enters adventure."""
    global points
    global player
    player = "name"
    points = 0

    greet()

    home_base()

#  game loop
    while choice >= 0:
        if choice == 0:  # 0 = exit game
            exit_game()

        if choice == 1:  # 1 = home base
            home_base()
            
        if choice == 2:  # 2 = search beaches
            points = search_beaches(points)
            
        if choice == 3:  # 3 = search jungle
            search_jungle()
            
    
def greet() -> None:
    """Greets the player and establishes name."""
    global player
    print(f"Welcome to Adventure Island! {ISLAND}")
    player = input("What is your name? ")
    print(f"Greetings, {player}! \nLegend has it, long ago, dread Pirate Roberts sailed here with his crew to hide his most valuable treasure-- the Crown of Emeralds. \nFor the past two centuries, adventurers like yourself have scoured this island to no avail...")


def exit_game() -> None:
    """Ends game."""
    global choice
    print(f"{player}, you have chosen to leave Adventure Island with {points} total adventure points.")
    print(f"Good luck in all your future adventures, {player}!")
    choice = -1


def home_base() -> None:
    """Allows player's choice of actions."""
    global points
    global choice
    print(f"{player}, you have {points} total adventure points.")
    print("How do you want to proceed?")
    print("2: I want to search the beaches. \n3: I want to search the jungle. \n0: I want to leave Adventure Island.")
    choice = int(input("Enter the number of your action: "))
    points = add_points(points)


def search_beaches(a: int) -> int:
    """Executes action that locates Emerald Crown."""
    global choice
    a = a + 1000
    print(f"{player}, you have chosen to search the beaches, and you now have {a} adventure points.")
    print(f"Congratulations, {player}! You found the Emerald Crown buried in the sand!")
    print("Would you like to... \n4: keep the Emerald Crown \n5: donate it to a museum")
    crown_choice: int = int(input("Enter the number of your action: "))

    if crown_choice == 4:
        a = a + 100
    if crown_choice == 5:
        a = a + 500
    
    choice = 1
    return a


def search_jungle() -> None:
    """Executes action that results in attack."""
    global points
    global choice
    print(f"{player}, you have chosen to search the jungle, and you now have {points} adventure points.")
    
    from random import randint
    x: int = randint(1, 3)
    if x == 1:
        print("You have been attacked by snakes after falling in a hidden jungle snake pit!")
        points = subtract_points(points)
    if x == 2:
        print("You have been attacked by spiders falling from the jungle canopy!")
        points = subtract_points(points)
    if x == 3:
        print("You have been attacked by wasps after disturbing their jungle nest!")
        points = subtract_points(points)

    choice = 1


def add_points(a: int) -> int:
    """Adds adventure points."""
    a = 10 + a
    return a


def subtract_points(a: int) -> int:
    """Subtracts adventure points."""
    a = a - 5
    return a

    
if __name__ == "__main__":
    main()