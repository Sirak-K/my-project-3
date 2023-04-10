# IMPORTS
from random import sample
import sys
import time

# VARIABLES

# Initialize hidden and guess boards for the various sizes
# HIDDEN_BOARD: Contains hidden ship locations
HIDDEN_BOARD_SMALL = [[" " for _ in range(4)] for _ in range(4)]
HIDDEN_BOARD_MEDIUM = [[" " for _ in range(6)] for _ in range(6)]
HIDDEN_BOARD_LARGE = [[" " for _ in range(8)] for _ in range(8)]

# GUESS_BOARD: Contains player's guesses (hits and misses)
GUESS_BOARD_SMALL = [[" " for _ in range(4)] for _ in range(4)]
GUESS_BOARD_MEDIUM = [[" " for _ in range(6)] for _ in range(6)]
GUESS_BOARD_LARGE = [[" " for _ in range(8)] for _ in range(8)]

# BOARD_SIZES_DICT: Maps size keys (s, m, l) to hidden/guess boards
BOARD_SIZES_DICT = {
    "s": {
        "HIDDEN_BOARD": HIDDEN_BOARD_SMALL,
        "GUESS_BOARD": GUESS_BOARD_SMALL
    },
    "m": {
        "HIDDEN_BOARD": HIDDEN_BOARD_MEDIUM,
        "GUESS_BOARD": GUESS_BOARD_MEDIUM
    },
    "l": {
        "HIDDEN_BOARD": HIDDEN_BOARD_LARGE,
        "GUESS_BOARD": GUESS_BOARD_LARGE
    }
}

# BOARD_COORDINATES: Maps letter coords to index values
BOARD_COORDINATES = {
 "A": 0,
 "B": 1,
 "C": 2,
 "D": 3,
 "E": 4,
 "F": 5,
 "G": 6,
 "H": 7}

# NUM_SHIPS: Constant for number of ships in game
NUM_SHIPS = 5


def print_fast(ltr):
    """
    Creates a fast typing effect
    """
    for letter in ltr:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


def print_slow(ltr):
    """
    Creates a slow typing effect.
    """
    for letter in ltr:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


# Game introduction
def intro():
    """
    This is the game introduction.
    """
    print("""\
    \033[92m
  ____        _   _   _           _     _
 |  _ \      | | | | | |         | |   (_)
 | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  ___
 |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \/ __|
 | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) \__ |
 |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/|___/
                                         | |
                                         |_|
\033[0m
""")

    print_slow("Welcome to battleships!\n")


def show_board(board: list) -> None:
    """
    Prints the game board to the console.

    Parameters:
    - board: a 2D list (game board).
    """
    board_scale = len(board[0])

    # Generate column headers (A, B, C, etc.) based on board_scale
    column_headers = "  "
    column_headers += " ".join([chr(i) for i in range(65, 65 + board_scale)])
    print(column_headers)

    # Print horizontal line
    print(" +{0}".format("-+" * board_scale))

    # Print board rows with row numbers
    for i, row in enumerate(board):
        print("{0}|{1}|".format(i + 1, "|".join(row)))

    # Print another horizontal line
    print(" +{0}".format("-+" * board_scale))


def show_boards(guess_board, hidden_board):
    """
    Prints the player's guess board and the hidden board to the console.

    Parameters:
    - guess_board: a 2D list (player's guess board).
    - hidden_board: a 2D list (hidden board with ship locations).
    """
    show_board(guess_board)


def create_ship(board) -> None:
    """
    Randomly places 5 ships on the game board.

    Parameters:
    - board: a 2D list (game board).
    """
    board_scale_x = len(board[0])
    board_scale_y = len(board)

    # Generate ship coordinates by sampling
    # unique (x, y) positions from the board.
    ship_coords = sample(
        [
            (x, y)
            for x in range(0, board_scale_x)
            for y in range(0, board_scale_y)
        ],
        NUM_SHIPS,
    )

    # Loop through the ship coordinates
    for ship_row, ship_column in ship_coords:
        board[ship_row][ship_column] = "S"


def get_board_coordinates(hidden_board) -> tuple:
    """
    Prompts the user to input the coordinates of a ship on the game board.

    Returns:
    - a tuple containing the row and column indices of the ship.
    """
    while True:
        try:
            row = input(f"Choose ROW 1-{len(hidden_board)}: ")
            row = row.strip().upper()
            print("You chose ROW: %s" % row)

            # Validate row input
            # Valid input is an integer between 1 and the length of the board.
            if not (row.isdigit() and 1 <= int(row) <= len(hidden_board)):
                raise ValueError("Invalid input. "
                                 "Please enter a valid row number.")

            row = int(row) - 1

            break

        except ValueError as e:
            print(e)

    while True:
        try:
            column_range = chr(64 + len(hidden_board[0]))
            column_prompt = f"Choose COLUMN A-{column_range}: "
            column = input(column_prompt)
            column = column.strip().upper()
            print(f"You chose COLUMN: {column}")

            # Validate column input
            if not (
                len(column) == 1 and
                ("A" <= column <= chr(64 + len(hidden_board[0])))
            ):

                raise ValueError(
                    "Invalid input. "
                    "Please enter a valid column letter."
                )

            column = ord(column) - 65

            break

        except ValueError as e:
            print(e)

    return row, column


def count_hits(board: list) -> int:
    """
    Returns the number of hits on the guess board

    Parameters:
    - board: a 2D list representing the guess board.

    Returns:
    - an integer representing the amount of "H"
    characters on the board.
    """
    return sum(1 for row in board for column in row if column == "H")


def reset_game_state(board_size):
    """
    Resets the game state for a new game

    Parameters:
    - board_size: a string as the board size
    ("s", "m", or "l").

    Returns:
    - a tuple containing the hidden_board, guess_board,
    TURNS_LEFT, and hit_count variables.
    """

    if board_size not in BOARD_SIZES_DICT:
        raise ValueError(f"Invalid board size: {board_size}")

    board_scale = len(BOARD_SIZES_DICT[board_size]["HIDDEN_BOARD"])

    # Create new boards using list comprehensions
    hidden_board = [[" "] * board_scale for _ in range(board_scale)]
    guess_board = [[" "] * board_scale for _ in range(board_scale)]

    TURNS_LEFT = 10
    hit_count = 0

    return hidden_board, guess_board, TURNS_LEFT, hit_count


def setup_game():
    """
    Sets up the game by initializing variables,
    prompting user for board size,
    and resetting the hidden and guess boards.

    Returns:
    - a tuple containing the hidden_board, guess_board,
      and TURNS_LEFT variables.
    """
    # Prompt user for board size and validate the input
    board_size = input("Please enter the board size "
                       "(s, m, l): ").lower().strip()
    while board_size not in ["s", "m", "l"]:
        board_size = (
            input("Invalid board size."
                  "Please enter again (s, m, l): ")
            .lower()
            .strip()
        )

    # Get the board and board scale based on the board size
    hidden_board = BOARD_SIZES_DICT[board_size]["HIDDEN_BOARD"]
    guess_board = BOARD_SIZES_DICT[board_size]["GUESS_BOARD"]

    # Reset boards and turns left
    hidden_board, guess_board, TURNS_LEFT, _ = reset_game_state(board_size)

    # Randomly place 5 ships on the hidden board
    create_ship(hidden_board)

    return hidden_board, guess_board, TURNS_LEFT


if __name__ == "__main__":
    play_again = "yes"
    while play_again.lower() == "yes":
        # Call the intro function here before prompting the user
        intro()
        # Setup game and initialize variables
        hidden_board, guess_board, TURNS_LEFT = setup_game()
        hit_count = 0

        # Main game loop
        while TURNS_LEFT > 0:
            show_boards(guess_board, hidden_board)
            print("Your turn! Guess a battleship location.")

            # Get player's guess and validate input
            row, column = get_board_coordinates(hidden_board)

            # Process the player's guess
            if guess_board[row][column] in ["H", "M"]:
                print("This coordinate has already been targeted. "
                      "Choose another!")
            elif hidden_board[row][column] == "S":
                print("HIT!")
                guess_board[row][column] = "H"
                hit_count += 1
                TURNS_LEFT -= 1

                # Check win condition
                if hit_count == NUM_SHIPS:
                    print("You win!")
                    break
            else:
                print("MISS!")
                guess_board[row][column] = "M"
                TURNS_LEFT -= 1

            # Display remaining turns
            print(f"You have {TURNS_LEFT} turns left.")

            # If player runs out of turns, end game and show results
            if TURNS_LEFT == 0:
                print("You ran out of turns.")
                print("Total Hits: " + str(hit_count))

        # Prompt user to play again or exit
        play_again = (
            input("Do you want to play again? (Yes or No): ").lower().strip()
        )
