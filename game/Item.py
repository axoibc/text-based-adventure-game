""" Objects for the text-based adventure game. """

from GameObject import GameObject
from game.Room import Room

class Item(GameObject):
    """ Class representing an item in the game and its actions."""

    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

    def drop(self, target_room : Room) -> str:
        self.location = target_room.name
        target_room.add_item(self)
        return f"You have dropped the {self.name}."

    def examine(self) -> str:
        return self.examine_text if self.examine_text else self.description

    def use(self, target : Room) -> str:
        if self.usage and target:
            self.usage["location"] = target.name
            if self.usage.get("room_state", False):
                target.update_room_state(self.usage.get("room_state", None))
            if self.contains:
                item_to_add = Item(self.contains["name"], **self.contains)
                target.add_item(item_to_add)
            return self.usage["success"]
        else:
            return self.usage["failure"]