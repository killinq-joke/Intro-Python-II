# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, poem):
        self.name = name
        self.poem = poem

    def __str__(self):
        return f'{self.name}'