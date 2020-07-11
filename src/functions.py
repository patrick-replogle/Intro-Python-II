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
