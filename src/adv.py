import sys
from room import Room
from player import Player
from item import Item
from functions import create_player_name, handle_input, validate_direction, take_item, drop_item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Candle", "It will light your way")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Rope", "Climb the tallest cliffs")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Sword", "Vanquish your enemies")]),

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
         \n{player.current_room.description}.\n")

    player.get_current_room_items()

    # * Waits for user input and decides what to do.
    user_input = input("\nWhat shall I do? ").split(" ")
    selection = handle_input(user_input)

    # If the user enters "q", quit the game.
    if len(selection) == 1 and selection[0] == "q":
        break
    # If the user enters a cardinal direction, attempt to move to the room there.
    elif len(selection) == 1 and selection[0] == "n":
        validate_direction(player, "n_to")
    elif len(selection) == 1 and selection[0] == "s":
        validate_direction(player, "s_to")
    elif len(selection) == 1 and selection[0] == "e":
        validate_direction(player, "e_to")
    elif len(selection) == 1 and selection[0] == "w":
        validate_direction(player, "w_to")
    elif len(selection) == 1 and selection[0] == "i":
        player.get_player_items()
    elif len(selection) == 2 and selection[0][0] == "t" or selection[0][0] == "g":
        take_item(player, selection)
    elif len(selection) == 2 and selection[0][0] == "d" or selection[0][0] == "":
        drop_item(player, selection)
    else:
        print("\nI don't understand")
