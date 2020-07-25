class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

    def on_take(self):
        print(f"\nYou have picked up the {self.name}")

    def on_drop(self):
        print(f"\nYou have dropped the {self.name}")
