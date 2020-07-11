import sys
from room import Room
from player import Player
from item import Item

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


# helper functions

def create_player_name(lst):
    if(len(lst) == 2):
        return lst[1]
    else:
        return 'Player One'


def handle_input(lst):
    for x in range(len(lst)):
        if len(lst) == 1:
            lst[x] = lst[x][0].lower()
        elif len(lst) == 2:
            lst[x] = lst[x].lower()
        else:
            break
    return lst


def validate_direction(player, direction):
    isValid = getattr(player.current_room, direction, None)
    if isValid:
        player.current_room = isValid
    else:
        print("\nMovement not allowed!")


def take_item(player, command):
    for item in player.current_room.items:
        if item.name.lower() == command[1]:
            player.take_item(item)
            player.current_room.remove_item(item)
            player.items[len(player.items) - 1].on_take(item.name)
            return
    else:
        print('\nThat item does not exist')


def drop_item(player, command):
    lst = player.items
    for i in range(len(lst)):
        if lst[i].name.lower() == command[1]:
            item = lst[i]
            player.items[i].on_drop(item.name)
            player.drop_item(item)
            player.current_room.add_item(item)
            return
    else:
        print('\nThat item does not exist')


    # Make a new player object that is currently in the 'outside' room.
player = Player(name=create_player_name(sys.argv),
                current_room=room["foyer"], items=[])

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
