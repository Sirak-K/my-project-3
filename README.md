# Battleships Game
![Python](https://img.shields.io/badge/Python-3.11.1-blue?logo=python)

View the deployed version of the Battleships application [here](https://my-project-3-battleships-73902a59a7ce.herokuapp.com/).

# Table of Contents
-   [Project Description](#project-description)
-   [How To Install](#how-to-install)
-   [How To Play](#how-to-play)
    -   [Objective](#objective)
    -   [Usage](#usage)
    -   [Game Setup](#game-setup)
    -   [Gameplay Mechanics](#gameplay-mechanics)
    -   [Game Controls](#game-controls)
    -   [Gameplay Features](#gameplay-features)
-   [Testing & Validation](#testing--validation)
    -   [Testing](#testing)
    -   [Validation](#validation)
-   [Deployment](#deployment)
-   [Credits](#credits)

# Project Description
This game is a Python implementation of the classic board game Battleships. The game involves two players, each of whom hides a number of ships on a grid. The other player then attempts to guess the locations of the ships by calling out coordinates on the grid. The game continues until all of one player's ships have been sunk.

# How To Install
1.  Clone the repository: git clone `https://github.com/Sirak-K/my-project-3.git`
2.  Navigate to the `my-project-3` directory: cd `my-project-3`
3.  Run the game: `python run.py`

# How To Play

### Objective
The objective of a Battleships game is to sink all of your opponent's ships before they sink yours.

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

This game has been thoroughly tested using the `unittest` framework. The testing code can be found in the `test_battleships.py` file and cover various aspects of the game's functionality.

**To run the tests, follow these steps:**

1. Make sure you have `unittest` installed. If not, you can install it using the following command:
   ```pip install unittest```

2. Navigate to the project directory where the `test_battleships.py` file is located.

3. Run the tests using the following command:
   ```python -m unittest test_battleships.py```

If all tests are successful, it will display "OK".

![testing_unittest](https://user-images.githubusercontent.com/122515678/230919251-06805f47-7af5-48f9-b6b2-0a1da17ad62c.png)

The testing code includes the following test cases:

1. **TEST-1**: Verifies the `show_board` function does not raise any unexpected exceptions.
2. **TEST-2**: Checks if the `create_ship` function places 5 ships on the board.
3. **TEST-3**: Validates that the `get_board_coordinates` function returns correct coordinates for valid input.
4. **TEST-4**: Tests if the `count_hits` function returns 0 for an empty board.
5. **TEST-5**: Ensures the `create_ship` function places 5 ships on a small board.
6. **TEST-6**: Confirms the `reset_game_state` function initializes the small board state correctly.
7. **TEST-7**: Validates the `reset_game_state` function initializes the medium board state correctly.
8. **TEST-8**: Verifies the `reset_game_state` function initializes the large board state correctly.
9. **TEST-9**: Checks if the `BOARD_SIZES_DICT` has the correct keys.
10. **TEST-10**: Asserts the `reset_game_state` function raises a `ValueError` for an invalid board size.

It is recommended to run the tests after any modifications to the codebase to ensure that all the functionality is working correctly.

Here's a table for the expected outcomes of the 10 test suites:

| Test Suite | Description                                                                                            | Expected Outcome                                                             |
|------------|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| TEST-1   | Verifies the `show_board` function does not raise any unexpected exceptions.                           | The `show_board` function should execute without raising any exceptions.     |
| TEST-2   | Checks if the `create_ship` function places 5 ships on the board.                                      | The `create_ship` function should place exactly 5 ships on the game board.   |
| TEST-3   | Validates that the `get_board_coordinates` function returns correct coordinates for valid input.       | The `get_board_coordinates` function should return the correct coordinates.  |
| TEST-4   | Tests if the `count_hits` function returns 0 for an empty board.                                       | The `count_hits` function should return 0 when called with an empty board.    |
| TEST-5   | Ensures the `create_ship` function places 5 ships on a small board.                                    | The `create_ship` function should place 5 ships on the small game board.      |
| TEST-6   | Confirms the `reset_game_state` function initializes the small board state correctly.                  | The `reset_game_state` function should correctly initialize the small board.  |
| TEST-7   | Validates the `reset_game_state` function initializes the medium board state correctly.                | The `reset_game_state` function should correctly initialize the medium board. |
| TEST-8   | Verifies the `reset_game_state` function initializes the large board state correctly.                  | The `reset_game_state` function should correctly initialize the large board.  |
| TEST-9   | Checks if the `BOARD_SIZES_DICT` has the correct keys.                                                 | The `BOARD_SIZES_DICT` should contain the keys "s", "m", and "l".             |
| TEST-10  | Asserts the `reset_game_state` function raises a ValueError for an invalid board size.                 | The `reset_game_state` function should raise a `ValueError` for invalid size. |

## Validation
### Tool used: [PEP-8 Linting Validator](https://pep8ci.herokuapp.com/#)

#### File: run.py
![linter_validation_game](https://github.com/Sirak-K/my-project-3/assets/122515678/f0bca064-3313-430a-8e3b-5257f79a6365)

#### File: test_battleships.py
![linter_validation_tests](https://github.com/Sirak-K/my-project-3/assets/122515678/78dd924d-c0f3-4fd4-a297-3d79047340d7)

## Deployment
Here are the steps to deploy the game on Heroku:

**1. Create a Heroku account:** If you don't have a Heroku account, go to [Heroku](https://www.heroku.com/) and sign up for an account.

**2. Install the Heroku CLI:** Download and install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) appropriate for your operating system.

**3. Log in to the Heroku CLI:** Open a terminal or command prompt and log in to the Heroku CLI using the following command:
   ```heroku login```

**4. Create a new Heroku app:** Navigate to the project directory and create a new Heroku app using the following command:
   ```heroku create <app-name>```
 * Replace `<app-name>` with the name for your Heroku app.

**5. Deploy the app:** Push the code to the Heroku remote repository to deploy the app using the following command:
   ```git push heroku main```

The Battleships game has now been successfully deployed to Heroku.

## Credits
- Inspired by Knowledge Mavens
https://github.com/gbrough/battleship/blob/main/single_player.py
