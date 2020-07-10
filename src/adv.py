import sys
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["Candle"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["Rope"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["Sword"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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


# helper functions

def create_player_name(lst):
    if(len(lst) == 2):
        return lst[1]
    else:
        return 'Player One'


def validate_direction(player, direction):
    isValid = getattr(player.current_room, direction, None)
    if isValid:
        player.current_room = isValid
    else:
        print("\nSuch foolishness will get you nowhere!")


# Make a new player object that is currently in the 'outside' room.

player = Player(name=create_player_name(sys.argv),
                current_room=room["outside"], items=[])

# Write a loop that:
#
while True:
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    print(
        f"\n{player.name}, you are currently located in the {player.current_room.name}. \
         \n{player.current_room.description}. \n ")

    # * Waits for user input and decides what to do.
    selection = input("What shall I do? ")
    selection = selection[0].lower()

    # If the user enters "q", quit the game.
    if selection == "q":
        break
    # If the user enters a cardinal direction, attempt to move to the room there.
    elif selection == "n":
        validate_direction(player, "n_to")
    elif selection == "s":
        validate_direction(player, "s_to")
    elif selection == "e":
        validate_direction(player, "e_to")
    elif selection == "w":
        validate_direction(player, "w_to")
    elif selection == "i":
        player.list_items()
    else:
        print("\nI don't understand")
