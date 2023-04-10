
# Project Description
This game is a Python implementation of the classic board game Battleships. The game involves two players, each of whom hides a number of ships on a grid. The other player then attempts to guess the locations of the ships by calling out coordinates on the grid. The game continues until all of one player's ships have been sunk.

# How To Install
1.  Clone the repository: git clone https://github.com/Sirak-K/my-project-3.git
2.  Navigate to the `my-project-3` directory: cd `my-project-3`
3.  Run the game: `python run.py`
# How To Play

### Objective
The objective of Battleships is to sink all of your opponent's ships before they sink yours.

### Usage
![bships_welcome](https://user-images.githubusercontent.com/122515678/230918805-e31498ef-fdb9-45d8-abea-60e05d3dda3b.jpg)

The game will prompt you to enter the board size at the start of each game. Choose from small (`s`), medium (`m`), or large (`l`) board sizes.
![gameplay_board_sizes](https://user-images.githubusercontent.com/122515678/230918842-02f1108c-b9ad-46f7-89b6-cbeae81f4a74.png)


### Game Setup
-   Each player gets their ships placed on their own grid without the other player seeing.
-   Ships can be placed horizontally or vertically.

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

### Gameplay Features
- Visual feedback system to keep track of gameplay information e.g turns left.
![gameplay_visual_feedback](https://user-images.githubusercontent.com/122515678/230919069-d37a1efe-47dc-4eb3-9727-f27e403d87a5.png)
- Option to instantly restart the application when a game has ended.
![gameplay_restart_game](https://user-images.githubusercontent.com/122515678/230919589-0637077e-7a0b-4372-9ed7-43b29548cf5f.png)

# Testing & Validation
## Testing
![testing_unittest](https://user-images.githubusercontent.com/122515678/230919251-06805f47-7af5-48f9-b6b2-0a1da17ad62c.png)


## Validation
### CI Python Linting Validator:
![linter_validation](https://user-images.githubusercontent.com/122515678/230919337-8e8605b3-53db-4b01-8446-0f6636c46fe1.png)



## Credits
- Inspired by Knowledge Mavens
https://github.com/gbrough/battleship/blob/main/single_player.py
