"""
Adventure Game
Author: Jacob McAleese
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""

# TODO: Create an empty list called `inventory` at the top of your code.
#       This will store items the player picks up during the game.

inventory = []



def welcome_player():
    #Welcome message and introduction
    print("Welcome to the adventure game!")
    print("Your journey begins here...")

    # Ask for the player's name
    player_name = input("What is your name, adventurer? ")

    # Use an f-string to display the same message in a more readable way
    print(f"Welcome, {player_name}! Your journey begins now.")
    return player_name



def describe_area():
    # Describe the starting area
    starting_area = """
    You find yourself in a dark forest...
    You see two paths ahead:
    A faint path lies ahead, leading deeper into the unknown...
    """
    print(starting_area)


def add_to_inventory(item):
    inventory.append(item)
    print("You picked up", item)

player_name = welcome_player() # return player name
describe_area()

while True:
    # Ask the player for their first decision
    decision = input("\t1. Take the left path into the dark woods\n"
                    "\t2. Take the right path to the mountain pass\n"
                    "\t3. Stay where you are\n"
                    "\t Type 'i' to view your inventory").lower()



    # conditional evaluate
    # Respond based on the player's decision
    if decision == "1": # = assignment operator == equivalent
        print("You go into the dark woods.")
        add_to_inventory("lantern")
    elif decision == "2":
        print("You go towards the mountain pass.") # Concatenation example
        add_to_inventory("map")
    elif decision == "3":
        print("Confused, you stand still, unsure of what to do.")
    elif decision == "i":
        print(inventory)
    else:
        print("That is not a valid choice")