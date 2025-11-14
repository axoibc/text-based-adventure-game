"""Main game loop for a text-based adventure game."""

import gameobject
import room
from game.commands import CommandWords, Directions
import yaml

from game.player import Player


class Game:
    rooms: room.Rooms
    items: gameobject.GameObjects
    player: Player

    def __init__(self, player: Player):
        self.rooms = room.Rooms()
        self.items = gameobject.GameObjects()
        self.player = player

    def load_rooms_and_items(self, file_path="game/data/rooms.yaml"):
        # This function would load rooms and items from a file or define them here.
        with open("game/data/items.yaml", "r") as file:
            item_data = yaml.safe_load(file)
            self.items.load(item_data)

        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
            self.rooms.load(data, self.items)


def main():
    player = Player("Hero")
    game = Game(player)
    game.load_rooms_and_items()
    # Start game loop
    current_room = game.rooms.get_starting_room()
    print(current_room)
    while True:
        command = (
            input("\nEnter a direction to move or 'quit' to exit: ").strip().lower()
        )
        if not command:
            continue
        cmd = command.split()
        if (
            cmd[0] in CommandWords._value2member_map_
            or cmd[0] in Directions._value2member_map_
        ):
            match cmd[0]:
                case CommandWords.QUIT.value:
                    print("Thanks for playing!")
                    break
                case CommandWords.EXAMINE.value | CommandWords.LOOK.value:
                    if len(cmd) > 1 and cmd[1] is not None:
                        examine_item = current_room.get_item(cmd[1]) or player.get_item(
                            cmd[1]
                        )
                        if examine_item:
                            print("-" * 20)
                            print(examine_item.examine())
                        else:
                            print(f"There is nothing special about that.")
                    else:
                        print("-" * 20)
                        print(current_room.examine())
                    continue
                case CommandWords.TAKE.value:
                    print("-" * 20)
                    if current_room.has_item(cmd[1]):
                        item = current_room.take_item(cmd[1])
                        player.add_item(item)
                    else:
                        print(f"There is no {cmd[1]} here to take.")
                    continue
                case CommandWords.DROP.value:
                    print("-" * 20)
                    if player.has_item(cmd[1]):
                        item = player.remove_item(cmd[1])
                        print(item.drop(current_room))
                    else:
                        print(f"You don't have a {cmd[1]} to drop.")
                    continue
                case CommandWords.INVENTORY.value:
                    print("-" * 20)
                    print(player.examine_inventory())
                    continue
                case CommandWords.HELP.value:
                    print(
                        "Available commands: go [direction], take [item], drop [item], examine [item], inventory, quit"
                    )
                    continue
                case CommandWords.GO.value:
                    if len(cmd) < 2:
                        print("Go where?")
                        continue
                    direction = cmd[1]
                    if direction in Directions._value2member_map_:
                        if (
                            current_room.get_exit(Directions(direction))
                            != current_room.name
                        ):
                            current_room = game.rooms.get_room(
                                current_room.get_exit(Directions(direction))
                            )
                            print(current_room)
                        else:
                            print("You can't go that way.")
                    else:
                        print("That's not a valid direction.")
                    continue
                case (
                    Directions.NORTH.value
                    | Directions.SOUTH.value
                    | Directions.EAST.value
                    | Directions.WEST.value
                    | Directions.UP.value
                    | Directions.DOWN.value
                ):
                    if current_room.get_exit(Directions(cmd[0])) != current_room.name:
                        current_room = game.rooms.get_room(
                            current_room.get_exit(Directions(cmd[0]))
                        )
                        print(current_room)
                    else:
                        print("You can't go that way.")
                    continue
                case CommandWords.USE.value | CommandWords.READ.value:
                    if len(cmd) < 2:
                        print("Use what?")
                        continue
                    item_name = cmd[1]
                    if player.has_item(item_name):
                        item = player.get_item(item_name)
                        print(f"You use the {item.name}.")
                        print(item.use(target=current_room, player=player))
                    else:
                        print(f"You don't have a {item_name} to use.")
                    continue
                case _:
                    print("Command not implemented yet.")
                    continue


if __name__ == "__main__":
    main()
