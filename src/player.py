# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return f"{self.name}, you are currently located in the {self.current_room}"

    def get_player_items(self):
        if len(self.items) == 0:
            print("\nYou have no items in your inventory")
        else:
            print('\nInventory:')
            for i in self.items:
                print(f"  {i}")

    def get_current_room_items(self):
        if len(self.current_room.items) > 0:
            print(f"\nItems in {self.current_room.name}")
            for i in self.current_room.items:
                print(f"  {i}")

    def take_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)
