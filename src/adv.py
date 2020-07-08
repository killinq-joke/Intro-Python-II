from player import Player
from room import Room
# Declare all the rooms
import textwrap



room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("narrow", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("treasure", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player(input("What's your name? "), "outside")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def start_game():

    while True:
        location = player1.location
        print(f"You are currently here: {location}")
        for line in textwrap.wrap(room[location].description):
            print(line)

        direction = input("Where do you want to go? (n/s/e/w) ")
        if direction == "q":
            print("Au revoir")
            break

        elif direction != "n" and direction != "s" and direction != "e" and direction != "w":
            print("Please enter a direction (n/s/e/w) ")

        else:
            if hasattr(room[location], f"{direction}_to"):
                print(getattr(room[location], f"{direction}_to").name)
                player1.location = getattr(
                    room[location], f"{direction}_to").name

            else:
                print("You died")
                break


if __name__ == "__main__":
    start_game()
