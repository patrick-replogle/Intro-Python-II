# helper functions

def create_player_name(lst):
    if len(lst) > 1:
        name = ""
        for i in range(1, len(lst)):
            name += lst[i] + " "
        return name.strip()
    else:
        return 'Player One'


def handle_input(lst):
    if len(lst) > 2:
        combined_input = ""
        for i in range(1, len(lst)):
            combined_input += lst[i] + " "
        lst = [lst[0][0], combined_input.strip()]
    return lst


def validate_direction(player, direction):
    if hasattr(player.current_room, direction):
        player.current_room = getattr(player.current_room, direction, None)
        player.print_player_location()
    else:
        print("\nThere is nothing in that direction!")


def take_item(player, command):
    for item in player.current_room.items:
        if item.name.lower() == command[1]:
            player.take_item(item)
            player.current_room.remove_item(item)
            player.items[len(player.items) - 1].on_take()
            return
    print('\nThat item is not in the room')


def drop_item(player, command):
    for i in range(len(player.items)):
        if player.items[i].name.lower() == command[1]:
            player.current_room.add_item(player.items[i])
            player.items[i].on_drop()
            player.drop_item(player.items[i])
            return
    print('\nThat item is not in your inventory')
