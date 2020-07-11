import sys
from room import Room
from player import Player
from item import Item
from functions import create_player_name, print_location, handle_input, validate_direction, take_item, drop_item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Stick", "It's better than nothing")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Rope", "Climb the tallest cliffs")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Sword", "Vanquish your enemies")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),

    'secret room': Room("Secret Room", """You've found the secret room North of the Treasure
Chamber. Reward yourself with treasures once thought to be lost. South of you is the main room of 
the treasure chamber.""", [Item("Gold Coins", "Fill your pockets with riches"),
                           Item("Crown", "The crown of a once great king"),
                           Item("Holy Grail", "Indiana Jones would be pleased")]),
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
room['treasure'].n_to = room['secret room']
room['secret room'].s_to = room['treasure']

# Make a new player object that is currently in the 'outside' room.
player = Player(name=create_player_name(sys.argv),
                current_room=room["outside"], items=[])

# print(f"\n{player.name}, you are in the {player.current_room.name}. \
#          \n{player.current_room.description}.")


print(f"\n{player.name}, you are in the {player.current_room.name}. \
         \n{player.current_room.description}.")

# Write a loop that:
#
while True:
    player.get_current_room_items()
    # Waits for user input and decides what to do.
    user_input = input("\nWhat shall I do? ").lower().split(" ")
    first_letter = user_input[0][0]
    selection = handle_input(user_input)

    # If the user enters "q", quit the game.
    if first_letter == "q":
        break
    # Prints the Prints the current room name and current description
    elif first_letter == "l":
        print_location(player)
    # If the user enters a cardinal direction, attempt to move to the room there.
    elif first_letter == "n":
        validate_direction(player, "n_to")
        print_location(player)
    elif first_letter == "s":
        validate_direction(player, "s_to")
        print_location(player)
    elif first_letter == "e":
        validate_direction(player, "e_to")
        print_location(player)
    elif first_letter == "w":
        validate_direction(player, "w_to")
        print_location(player)
    elif first_letter == "i":
        player.get_player_items()
    # If user enters "take" or "get" followed by item an name, the item will be added to inventory
    elif first_letter == "t" or first_letter == "g":
        take_item(player, selection)
    # If user enters "drop" or "remove" followed by an item name, the item will be removed and added to the current room
    elif first_letter == "d" or first_letter == "r":
        drop_item(player, selection)
    else:
        print("\nI don't understand")
