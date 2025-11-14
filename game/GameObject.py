from abc import ABC

from game.player import Player


class GameObjects:
    items: dict[str, GameObject]

    def __init__(self):
        self.items = {}

    def load(self, data):
        incoming_items = data.get("items", {})
        for item_name, item_data in incoming_items.items():
            self.items[item_name] = GameObject(item_name, **item_data)

        for item_name, item_data in incoming_items.items():
            if item_data.get("contains", []):
                for contained_item in item_data["contains"]:
                    self.items[item_name].add_object(self.items[contained_item])

    def get_object(self, item_name: str) -> GameObject | None:
        return self.items.get(item_name)


class GameObject(ABC):

    name: str
    description: str
    location: str
    examine_text: str
    contains: str
    usage: dict
    objects: dict[str, GameObject]

    def __init__(self):
        self.name = ""
        self.description = ""
        self.location = ""
        self.examine_text = ""
        self.contains = []
        self.usage = {}
        self.takeable_items = []
        self.objects = {}

    def __init__(self, name, **kwargs):
        self.name = name
        self.description = kwargs.get("description", "")
        self.location = kwargs.get("location", "")
        self.examine_text = kwargs.get("examine_text", "")
        self.contains = kwargs.get("contains", [])
        self.usage = kwargs.get("use", {})
        self.takeable_items = kwargs.get("takeable_items", [])
        self.objects = {}

    def __str__(self):
        return f"{self.name}: {self.description}"

    def add_object(self, item: GameObject):
        self.objects[item.name] = item

    def remove_object(self, item_name: str):
        if item_name in self.objects:
            del self.objects[item_name]

    def drop(self, location: GameObject):
        """Drop this object in a target GameObject location"""
        location.add_item(self)
        self.location = location.name
        return f"You dropped the {self.name} in the {location.name}."

    def take(self):
        self.location = "inventory"
        return f"You took the {self.name}."

    def examine(self) -> str:
        return self.examine_text if self.examine_text else self.description

    def use(self, target: GameObject, player: Player) -> str:
        """Use this object on a target GameObject and Player"""
        if self.usage:
            location = self.usage.get("location", None)
            if location and target.name == location:
                if self.usage.get("room_state", False):
                    target.update_room_state(self.usage.get("room_state", None))

            # if the object contains other objects, transfer them to the player when used
            if self.objects:
                for obj in self.objects.values():
                    print(f"(You took {obj.name})")
                    player.add_item(obj)
                    print(obj.use(target, player))
                if obj:
                    self.remove_object(obj.name)

            return self.usage["success"]
        else:
            return self.usage["failure"]
