"""Directions for the text-based adventure game."""

import enum


class Directions(enum.Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"
    UP = "up"
    DOWN = "down"


DIRECTIONS = [
    Directions.NORTH,
    Directions.SOUTH,
    Directions.EAST,
    Directions.WEST,
    Directions.UP,
    Directions.DOWN,
]


class CommandWords(enum.Enum):
    EXAMINE = "examine"
    GO = "go"
    TAKE = "take"
    DROP = "drop"
    LOOK = "look"
    USE = "use"
    HELP = "help"
    INVENTORY = "inventory"
    QUIT = "quit"
    READ = "read"


COMMANDS = [
    CommandWords.EXAMINE,
    CommandWords.TAKE,
    CommandWords.DROP,
    CommandWords.LOOK,
    CommandWords.USE,
    CommandWords.INVENTORY,
    CommandWords.QUIT,
    CommandWords.READ,
    Directions.NORTH,
    Directions.SOUTH,
    Directions.EAST,
    Directions.WEST,
    Directions.UP,
    Directions.DOWN,
]


def opposite_direction(direction: Directions) -> Directions:
    opposites = {
        Directions.NORTH: Directions.SOUTH,
        Directions.SOUTH: Directions.NORTH,
        Directions.EAST: Directions.WEST,
        Directions.WEST: Directions.EAST,
        Directions.UP: Directions.DOWN,
        Directions.DOWN: Directions.UP,
    }
    return opposites.get(direction)
