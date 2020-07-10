# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return f"{self.name}, you are currently located in the {self.current_room}"

    def list_items(self):
        if len(self.items) == 0:
            print("\nYou have no items in your inventory")
        else:
            for i in self.items:
                print(i)

    def take_item(self, item):
        self.items.append(item)
        return self.items

    def drop_item(self, item):
        self.items.remove(item)
        return self.items
