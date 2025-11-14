"""Room class for a text-based adventure game."""

from game.commands import Directions, opposite_direction
from gameobject import GameObject, GameObjects


class Rooms:
    rooms: dict[str, Room]

    def __init__(self):
        self.rooms = {}

    def load(self, data, items: GameObjects):
        self.rooms = {}
        for room_name, room_data in data["rooms"].items():
            room = Room(room_name, room_data)
            self.rooms[room_name] = room
            for item_name in items.items:
                item = items.get_object(item_name)
                if item and item.location == room_name:
                    room.add_item(item)

        for room_name, room_data in data["rooms"].items():
            for direction, to_room in room_data["exits"].items():
                if self.rooms.get(to_room):
                    print(f"Linking {room_name} to {to_room} via {direction}")
                    self.rooms[room_name].add_exit(Directions(direction), to_room)
                    self.rooms[to_room].add_exit(
                        opposite_direction(Directions(direction)), room_name
                    )

    def get_room(self, room_name: str) -> Room | None:
        return self.rooms.get(room_name)

    def get_starting_room(self) -> Room | None:
        for room in self.rooms.values():
            if room.starting_room:
                return room
        return None

    def has_room(self, room_name):
        return self.rooms.get(room_name) is not None

    def __str__(self):
        return "\n".join(str(room) for room in self.rooms.values())


class Room(GameObject):

    exits: dict[Directions, str]
    starting_room: bool
    room_state: str
    inventory: list[GameObject]
    takeable_items: list[str]

    def __init__(self, name, room_data):
        super().__init__(name, **room_data)
        self.exits = {dir.value: None for dir in Directions}
        for direction, to_room in room_data["exits"].items():
            self.exits[Directions(direction)] = to_room
        self.starting_room = room_data.get("starting_room", False)
        self.room_state = room_data.get("starting_room", "locked")
        self.inventory = []

    def add_exit(self, direction: Directions, room: Room):
        self.exits[direction.value] = room

    def get_exit(self, direction: Directions):
        if self.exits.get(direction.value):
            return self.exits.get(direction.value)
        return self.name

    def add_item(self, item: GameObject):
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
        if self.inventory:
            item_list = ", ".join(item.name for item in self.inventory)
            return f"{self.description}\nYou see the following items: {item_list}"
        else:
            return f"{self.description}"

    def __str__(self):
        dirs = [dir for dir in Directions if self.exits[dir.value] is not None]
        exit_names = ", ".join(dirs[i].value for i in range(len(dirs)))
        items_in_room = (
            ", ".join(item.name for item in self.inventory)
            if self.inventory
            else "None"
        )
        return f"{self.name}\n\n{self.description}\n\nExits: {exit_names}\n\nItems in room: {items_in_room}"
