""" Room class for a text-based adventure game. """
from commands import Directions
from GameObject import GameObject
    
class Room(GameObject):

    exits: dict[Directions, str]
    starting_room: bool
    room_state: str
    inventory: list[GameObject]

    def __init__(self, name, room_data):
        super().__init__(name, **room_data)
        self.exits = { dir.value: None for dir in Directions }
        for direction, to_room in room_data["exits"].items():
            self.exits[Directions(direction)] = to_room
        self.starting_room = False
        self.room_state = "locked"
        self.inventory = []

    def add_exit(self, direction: Directions, room: Room):
        self.exits[direction.value] = room

    def get_exit(self, direction: Directions):
        if self.exits.get(direction.value):
            return self.exits.get(direction.value)
        return self.name

    def add_item(self, item : GameObject):
        self.inventory.append(item)
    
    def has_item(self, item_name: str) -> bool:
        return self.get_item(item_name) is not None

    def get_item(self, item_name: str) -> GameObject | None:
        for item in self.inventory:
            if item.name == item_name:
                return item
        return None

    def take_item(self, item_name: str) -> GameObject | None:
        item = self.get_item(item_name)
        if not item:
            print(f"There is no {item_name} here to take.")
            return None
        self.inventory.remove(item)
        print(f"You have taken the {item_name}.")
        return item
    
    def use_item(self, item_name: str) -> str:
        if not self.has_item(item_name):
            return f"There is no {item_name} here to use."
        item = self.get_item(item_name)
        return item.use(self)

    def set_starting_room(self, is_starting: bool):
        self.starting_room = is_starting

    def update_room_state(self, new_state: str):
        self.room_state = new_state  

    def examine(self) -> str:
        item_list = ', '.join(item.name for item in self.inventory) if self.inventory else "None"
        if item_list:
            return f"{self.description}\nYou see the following items: {item_list}"
        else:
            return f"{self.description}"

    def __str__(self):
        dirs = [dir for dir in Directions if self.exits[dir.value] is not None]
        exit_names = ', '.join(dirs[i].value for i in range(len(dirs)))
        items_in_room = ', '.join(item.name for item in self.inventory) if self.inventory else "None"
        return f"{self.name}\n\n{self.description}\n\nExits: {exit_names}\n\nItems in room: {items_in_room}"