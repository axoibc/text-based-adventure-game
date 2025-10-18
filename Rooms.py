from commands import Directions, opposite_direction
from Room import Room


class Rooms():
    def __init__(self, data, items):
        self.rooms = {}
        incoming_rooms = data["rooms"]
        for room_name, room_data in incoming_rooms.items():
            self.rooms[room_name] = Room(room_name, room_data)
            room_objs = room_data.get("takeable_items")
            if room_objs:
                for item_name in room_objs:
                    obj = items.get_item(item_name)
                    if obj:
                        self.rooms[room_name].add_item(obj)
                    else:
                        print(f"Warning: Item {item_name} not found for room {room_name}")

            if room_data.get("starting_room"):
                self.rooms[room_name].set_starting_room(True)

        for room_name, room_data in incoming_rooms.items():
            for direction, to_room in room_data["exits"].items():
                if self.rooms.get(to_room):
                    print(f"Linking {room_name} to {to_room} via {direction}")
                    self.rooms[room_name].add_exit(Directions(direction), to_room)
                    self.rooms[to_room].add_exit(opposite_direction(Directions(direction)), room_name)
        
        

    def has_room(self, room_name):
        return self.rooms.get(room_name) is not None

    def get_room(self, room_name):
        return self.rooms.get(room_name)
    
    def get_starting_room(self):
        for room in self.rooms.values():
            if hasattr(room, 'starting_room') and room.starting_room:
                return room
        return None
    
    def __str__(self):
        return "\n".join(str(room) for room in self.rooms.values())