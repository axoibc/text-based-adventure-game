""" Module for managing game objects. """
from Item import Item

class Objects():
    """ Class to manage all game items. """

    def __init__(self, data):
        self.items = {}
        incoming_items = data.get("items", {})
        for item_name, item_data in incoming_items.items():
            self.items[item_name] = Item(item_name, **item_data)

    def get_item(self, item_name):
        return self.items.get(item_name)

    def __str__(self):
        return "\n".join(str(item) for item in self.items.values())