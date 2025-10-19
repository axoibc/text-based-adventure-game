# Text Game Project

Welcome to the Text Game project! This repository contains the source code and resources for the game.

## Features

- Proof of concept for dealing with command input and navigation
- Play ground for adding new concepts to the game

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/axoibc/game.git
    ```
2. Install dependencies:
    ```bash
    # uses poetry to install dependencies
    poetry install
    ```
3. Run the game:
    ```bash
    poetry run python game/main.py
    ```
# Playthrough

Currently the game has several rooms in which you can interact with objects in those rooms.

Here is an example play through testing out objects containing other objects:
```
foyer

You are standing in the foyer of a grand mansion. A chandelier hangs above you.

Exits: north, east

Items in room: key

Enter a direction to move or 'quit' to exit: take key
--------------------
You have taken the key.

Enter a direction to move or 'quit' to exit: go north
library

You are in a quiet library filled with shelves of books.

Exits: south

Items in room: book

Enter a direction to move or 'quit' to exit: drop key
--------------------
You dropped the key in the library.

Enter a direction to move or 'quit' to exit: examine
--------------------
You are in a quiet library filled with shelves of books.
You see the following items: book, key

Enter a direction to move or 'quit' to exit: take key
--------------------
You have taken the key.

Enter a direction to move or 'quit' to exit: take book
--------------------
You have taken the book.

Enter a direction to move or 'quit' to exit: examine
--------------------
You are in a quiet library filled with shelves of books.

Enter a direction to move or 'quit' to exit: drop book
--------------------
You dropped the book in the library.

Enter a direction to move or 'quit' to exit: drop key
--------------------
You dropped the key in the library.

Enter a direction to move or 'quit' to exit: use book
You don't have a book to use.

Enter a direction to move or 'quit' to exit: take book
--------------------
You have taken the book.

Enter a direction to move or 'quit' to exit: use book
You use the book.
(You took note)
The note reads: 'The key unlocks more than just doors...'
You find a hidden note inside the book.

Enter a direction to move or 'quit' to exit: drop book
--------------------
You dropped the book in the library.

Enter a direction to move or 'quit' to exit: inventory
--------------------
You have the following items: note

Enter a direction to move or 'quit' to exit: examine note
--------------------
A small handwritten note.

Enter a direction to move or 'quit' to exit: use note
You use the note.
The note reads: 'The key unlocks more than just doors...'

Enter a direction to move or 'quit' to exit: drop note
--------------------
You dropped the note in the library.

Enter a direction to move or 'quit' to exit: examine
--------------------
You are in a quiet library filled with shelves of books.
You see the following items: key, book, note

Enter a direction to move or 'quit' to exit: quit
Thanks for playing!
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.
