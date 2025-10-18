from abc import ABC


class GameObject(ABC):
    name: str
    description: str
    location: str
    examine_text: str
    contains: str
    usage: dict
    takeable_items: list[str]

    def __init__(self, name, **kwargs):
        self.name = name
        self.description = kwargs.get("description", "")
        self.location = kwargs.get("location", "")
        self.examine_text = kwargs.get("examine_text", "")
        self.contains = kwargs.get("contains", "")
        self.usage = kwargs.get("use", {})
        self.takeable_items = kwargs.get("takeable_items", [])
        
    def __str__(self):
        return f"{self.name}: {self.description}"

    def examine(self):
        if self.examine_text:
            return self.examine_text or self.description
        return f"You see nothing special about the {self.name}."
    def use(self, target):
        return f"You can't use the {self.name} here."
    def drop(self, location):
        self.location = location.name
        return f"You dropped the {self.name} in the {location.name}."
    def take(self):
        self.location = "inventory"
        return f"You took the {self.name}."