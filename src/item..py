class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        return f"You have picked up {self.name} when you pick up an item."