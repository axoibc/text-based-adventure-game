""" Inventory class for a text-based adventure game. """
from Item import Item


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item: Item):
        self.items[item.name] = item

    def remove_item(self, item: str) -> Item:
        if self.has_item(item):
            return self.items.pop(item, None)
        else:
            print(f"No item named {item} in inventory.")
            return None

    def has_item(self, item: str) -> bool:
        return item in self.items.keys()
    
    def get_item(self, item: str) -> Item:
        return self.items.get(item, None)

    def __str__(self):
        if not self.items:
            return "Empty."
        return  self.items.values()

class PlayerInventory(Inventory):
    def __init__(self):
        super().__init__()

    def __str__(self):
        if not self.items:
            return "Your inventory is empty."
        item_list = ', '.join(self.items.keys())
        return f"Inventory: {item_list}"
