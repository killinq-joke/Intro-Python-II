from player import Player
from room import Room
# Declare all the rooms
import textwrap


room = {
    'outside':  Room("outside", "Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["flashlight", "rock"]),

    'foyer':    Room("foyer", "Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["cutter"]),

    'overlook': Room("overlook", "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["battery"]),

    'narrow':   Room("narrow", "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["rock"]),

    'treasure': Room("treasure", "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["empty treasure"]),
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
player1 = Player(input("What's your name? "), "outside", [])
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
        current_room = player1.current_room
        print(f"\nYou are currently here: {room[current_room]}\n")
        for line in textwrap.wrap(room[current_room].description):
            print(line)

        command = input("\nEnter a command: ")
        command = command.lower().strip()
        if command == "q":
            print("Au revoir")
            break

        elif command == "help":
            print("Go north: n")
            print("Go south: s")
            print("Go east: e")
            print("Go west: w")
            print("Examine room: exam")
            print("Get: get")
            print("Drop: drop")
            print("Inventory: i")

        elif command == "exam":
            print(*room[current_room].items, sep=", ")

        elif command.split(' ', 1)[0] == "get" or command.split(' ', 1)[0] == "take" and command != command.split(' ', 1)[0]:
            item = command.split(" ", 1)[1]
            if item in room[current_room].items:
                player1.items.append(item)
                room[current_room].items.remove(item)
                print(f"You picked: {item}")

            else:
                print(f"There is no {item} here")

        elif command.split(' ', 1)[0] == "drop" and command != command.split(' ', 1)[0]:
            item = command.split(" ", 1)[1]
            if item in player1.items:
                room[current_room].items.append(item)
                player1.items.remove(item)
                print(f"You dropped: {item}")
            
            else:
                print("You can't drop an item you don't have")

        elif command == "i" or command == "inventory":
            print(*player1.items, sep =", ")

        elif command != "n" and command != "s" and command != "e" and command != "w":
            print("Please enter a correct command (help) ")

        else:
            if hasattr(room[current_room], f"{command}_to"):
                player1.current_room = getattr(
                    room[current_room], f"{command}_to").location

            else:
                print("You died")
                break


if __name__ == "__main__":
    start_game()
