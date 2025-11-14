import gameobject


class Player:
    """Class representing the player in the game."""

    name: str
    inventory: dict[str, gameobject.GameObject]

    def __init__(self, name: str):
        self.name = name
        self.inventory = {}

    def add_item(self, item: gameobject.GameObject):
        self.inventory[item.name] = item

    def remove_item(self, item_name: str):
        return self.inventory.pop(item_name, None)

    def has_item(self, item_name: str) -> bool:
        return item_name in self.inventory

    def get_item(self, item_name: str):
        return self.inventory.get(item_name, None)

    def examine_inventory(self) -> str:
        if not self.inventory:
            return "Your inventory is empty."
        item_list = ", ".join(self.inventory.keys())
        return f"You have the following items: {item_list}"

    def __str__(self):
        if not self.inventory:
            return "Your inventory is empty."
        item_list = ", ".join(self.inventory.keys())
        return f"Inventory: {item_list}"
