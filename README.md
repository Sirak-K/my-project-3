
# Project Description
This game is a Python implementation of the classic board game Battleships. The game involves two players, each of whom hides a number of ships on a grid. The other player then attempts to guess the locations of the ships by calling out coordinates on the grid. The game continues until all of one player's ships have been sunk.

# How To Install
1.  Clone the repository: git clone https://github.com/your_username/battleships.git
2.  Navigate to the `battleships` directory: cd battleships
3.  Run the game: python run.py
# How To Play

### Objective
The objective of Battleships is to sink all of your opponent's ships before they sink yours.

### Usage
The game will prompt you to enter the board size at the start of each game. Choose from small (`s`), medium (`m`), or large (`l`) board sizes.

### Game Setup
-   Each player gets their ships placed on their own grid without the other player seeing.
-   Ships can be placed horizontally or vertically.
-   Ships must be placed entirely within the grid.
-   Players cannot place ships adjacent to each other.

### Gameplay Mechanics
-   Players take turns guessing the location of the other player's ships by calling out a coordinate on the grid.
-   If the guessed coordinate contains a ship, it is a hit. If not, it is a miss.
-   If a ship is hit, the attacking player gets to take another turn.
-   When a ship is hit in all of its squares, it is sunk.
-   The game continues until all of one player's ships have been sunk.

### Game Controls
-   Use the keyboard to input your guesses.
-   Row numbers range from 1 to the length of the board (e.g. 1-8 for a large board).
-   Column letters range from A to the last letter of the alphabet corresponding to the length of the board e.g. A-H for a large board and A-D for a small board.

## Testing & Validation
## Testing

![Alt Text](game_tests.png)



## Validation
### CI Python Linting Validator:

  

## Deployment


## Credits
