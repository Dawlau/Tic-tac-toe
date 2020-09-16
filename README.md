# Tictactoe (Linux version)

This is a Tic-tac-toe game developed with [Python 3.8](https://www.python.org/) and [Pygame](https://www.pygame.org/news).

Most of the project was done using just basic Python. Pygame was used for GUI and Event Handling.

## Features

The project contains 3 main parts: the home screen, the singleplayer mode and the multiplayer mode.

In every mode of playing you can go back to the home screen by pressing "Esc". Also, you can restart the current game by pressing "R" and you can quit the game by pressing "Q".

### Homescreen

It gives access to the two ways of playing by clicking on the respective text.

### Singleplayer

Here, you are facing an unbeatable bot that is playing as O. 
You are playing as X and can make a move by clicking an empty cell in the grid.

Good luck!

Notes:

1. The bot was programmed using the [minimax algorithm](https://en.wikipedia.org/wiki/Minimax) and optimized using [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).
This way it is making optimal moves in no time.

2. If you somehow manage to beat it please report it by sending a screenshot of the game to: blahoviciandrei1@gmail.com

### Multiplayer

In this mode you are to play with a friend from the same PC. The GUI is very intuitive as
you know every time whose turn is. As in singleplayer you make moves by clicking an empty cell in the grid.
At the end you will see a text of the winner or a message that says "It's a tie!".

## Requirements

In order to play you have got to first install:

1. [Python3](https://docs.python-guide.org/starting/install3/linux/)
2. [Pygame](https://www.pygame.org/wiki/GettingStarted)

The installation varies from distribution to distribution. Hopefully the links from above are useful to you.

## How to run

1. Open the main directory of the project (in here you should find a file called "run.sh")
2. Open the terminal in the current directory
3. Run the command "./run.sh"

## Final notes

I hope you enjoy playing this Tic-tac-toe game. If you find any bugs, feel free to submit them to blahoviciandrei1@gmail.com
