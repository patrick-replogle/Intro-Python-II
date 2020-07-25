from item import Item


class Light(Item):
    def __init__(self, name, description, brightness):
        super().__init__(name, description)
        self.brightness = brightness
