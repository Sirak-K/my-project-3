from random import randint

# LIST: GUESSES
HIDDEN_BOARD_small = [[" "] * 4 for x in range(4)]
HIDDEN_BOARD_medium = [[" "] * 6 for x in range(6)]
HIDDEN_BOARD_large = [[" "] * 8 for x in range(8)]

# LIST: HITS & MISSES
GUESS_BOARD_small = [[" "] * 4 for i in range(4)]
GUESS_BOARD_medium = [[" "] * 6 for i in range(6)]
GUESS_BOARD_large = [[" "] * 8 for i in range(8)]

# DICTIONARY
# DICTIONARY KEYS: small, medium, large
# DICTIONARY KEYS: HIDDEN_BOARD, GUESS_BOARD
BOARD_SIZES_DICT = {
    "s": {"HIDDEN_BOARD": HIDDEN_BOARD_small,
          "GUESS_BOARD": GUESS_BOARD_small},
    "m": {"HIDDEN_BOARD": HIDDEN_BOARD_medium,
          "GUESS_BOARD": GUESS_BOARD_medium},
    "l": {"HIDDEN_BOARD": HIDDEN_BOARD_large,
          "GUESS_BOARD": GUESS_BOARD_large}
}

# BOARD COORDINATES
BOARD_COORDINATES = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7
}

# Define a constant variable for the number of ships
NUM_SHIPS = 5

hit_count = 0

# ----------------- FUNCTIONS START ---------------- #


def show_board(board: list) -> None:
    """
    Prints the game board to the console.

    Parameters:
    - board: a 2D list representing the game board.

    """

    # PRINT A HEADER
    board_scale = len(board[0])

    # Generate column headers (A, B, C, etc.)
    # based on the board_scale by converting ASCII values to characters
    column_headers = "  "
    column_headers += " ".join(chr(i) for i in range(65, 65 + board_scale))
    print(column_headers)

    # PRINT A HORIZONTAL LINE
    print(" +" + "-+" * board_scale)

    # Use a list comprehension to generate the row strings
    for i, row in enumerate(board):
        print(f"{i+1}|{'|'.join(row)}|")

    # PRINT A HORIZONTAL LINE
    print(" +" + "-+" * board_scale)


def create_ship(board, board_size, used_coords) -> None:
    """
    Randomly places 5 ships on the game board.

    Parameters:
    - board: a 2D list representing the game board.
    - board_size: a string representing the board size ("s", "m", or "l").
    """
    # Create a set to store used coordinates
    used_coords = set()

    # Calculate the size of the board
    # VARIABLES DEFINED
    if board_size == "s":
        board_scale_x = 4
        board_scale_y = 4
    elif board_size == "m":
        board_scale_x = 6
        board_scale_y = 6
    elif board_size == "l":
        board_scale_x = 8
        board_scale_y = 8
    else:
        raise ValueError("Invalid board size. Please choose s, m, or l.")

    print("Creating Ships ", end="")
    for ship in range(NUM_SHIPS):
        if ship == NUM_SHIPS - 1:
            print(ship + 1)
        else:
            print(ship + 1, end="-")

        while True:
            # Generate random coordinates
            ship_row, ship_column = randint(0, board_scale_y - 1), randint(
                0, board_scale_x - 1
            )

            # Check if coordinates have been used before
            if (ship_row, ship_column) in used_coords:
                continue

            # If coordinates have not been used before,
            # add them to used_coords and
            # place the ship
            used_coords.add((ship_row, ship_column))

            if board[ship_row][ship_column] == " ":
                board[ship_row][ship_column] = "S"
                break


def get_board_coordinates(hidden_board) -> tuple:
    """
    Prompts the user to input the coordinates of a ship on the game board.

    Returns:
    - a tuple containing the row and column indices of the ship.
    """
    while True:
        try:
            row = input("Choose ROW 1-{}: ".format(len(hidden_board)))
            row = row.strip().upper()
            print("You chose ROW: %s" % row)

            # VALIDATE INPUT: ROW
            if not (row.isdigit() and 1 <= int(row) <= len(hidden_board)):
                raise ValueError(
                    "Invalid input. " "Please enter a valid column letter."
                )

            row = int(row) - 1

            break

        except ValueError as e:
            print(e)

    while True:
        try:
            column = input(
                f"Choose COLUMN A-{chr(64 + len(hidden_board[0]))}: "
            )
            column = column.strip().upper()
            print("You chose COLUMN: %s" % column)

            # VALIDATE INPUT: COLUMN
            if not (
                len(column) == 1
                and "A" <= column <= chr(64 + len(hidden_board[0]))
            ):
                raise ValueError(
                    "Invalid input. " "Please enter a valid column letter."
                )

            column = ord(column) - 65

            break

        except ValueError as e:
            print(e)

    return row, column


def hit_tracker(board: list) -> int:
    """
    Returns the number of hits on the
    guess board and updates the hit_count variable.

    Parameters:
    - board: a 2D list representing the guess board.

    Returns:
    - an integer representing the number of "X"
    characters on the board.
    """

    hit_count = 0

    for row in board:

        for column in row:

            if column == "H":
                hit_count += 1

    return hit_count


def reset_game_state(board_sizes):
    """
    Functionality
    Resets the game state for a new game by
    initializing necessary variables
    and clearing the hidden and guess boards.

    Parameters:
    - board_sizes: a string representing the board size
    ("s", "m", or "l").

    Returns:
    - a tuple containing the hidden_board, guess_board,
    TURNS_LEFT, and hit_count variables.
    """
    hidden_board = BOARD_SIZES_DICT[board_sizes]["HIDDEN_BOARD"]
    guess_board = BOARD_SIZES_DICT[board_sizes]["GUESS_BOARD"]
    TURNS_LEFT = 3
    hit_count = 0

    # Reset hidden_board and guess_board using a list comprehension
    hidden_board[:] = [[" "] * len(hidden_board[0]) for _ in hidden_board]
    guess_board[:] = [[" "] * len(guess_board[0]) for _ in guess_board]

    return hidden_board, guess_board, TURNS_LEFT, hit_count


# NEW FUNCTION
def setup_game(board_size):
    """
    Sets up the game by initializing necessary variables,
    prompting user for board size,
    and resetting the hidden and guess boards.

    Returns:
    - a tuple containing the hidden_board, guess_board,
      and TURNS_LEFT variables.
    """

    board_size = input(
        "Please enter the board size (s, m, l): "
    ).lower().strip()
    while board_size not in ["s", "m", "l"]:
        board_size = (
            input("Invalid board size. "
                  "Please enter again (s, m, l): ")
            .lower()
            .strip()
        )

    # Get the board and board scale based on the board size
    hidden_board = BOARD_SIZES_DICT[board_size]["HIDDEN_BOARD"]
    guess_board = BOARD_SIZES_DICT[board_size]["GUESS_BOARD"]
    TURNS_LEFT = 3

    # Create sets to store used coordinates for ship placement
    used_coords = set()

    # Reset hidden_board and guess_board using a list comprehension
    hidden_board[:] = [[" "] * len(hidden_board[0]) for _ in hidden_board]
    guess_board[:] = [[" "] * len(guess_board[0]) for _ in guess_board]

    # Randomly place 5 ships on the hidden board
    create_ship(hidden_board, board_size, used_coords)

    return hidden_board, guess_board, TURNS_LEFT


if __name__ == "__main__":
    play_again = "yes"
    while play_again.lower() == "yes":

        hidden_board, guess_board, TURNS_LEFT = setup_game("")
        hit_count = 0

        while TURNS_LEFT > 0:

            show_board(guess_board)
            show_board(hidden_board)
            print("Your turn! Guess a battleship location.")

            row, column = get_board_coordinates(hidden_board)

            if guess_board[row][column] in ["H", "M"]:
                print("This coordinate has already been targeted. "
                      "Choose another!")
            elif hidden_board[row][column] == "S":
                print("HIT!")
                guess_board[row][column] = "H"
                hit_count += 1

                # Check win condition
                if hit_count == NUM_SHIPS:
                    print("You win!")
                    break
            else:
                print("MISS!")
                guess_board[row][column] = "M"
                TURNS_LEFT -= 1
                # Check win condition
                # If the player hits all # ships, end the game
                if hit_count == NUM_SHIPS:
                    print("You win!")
                    break

            # PRINT THE NUMBER of turns remaining
            print("You have " + str(TURNS_LEFT) + " turns left.")

            # IF THE USER has run out of turns,
            # Print a failure message and exit the loop.
            if TURNS_LEFT == 0:
                print("You ran out of turns.")
                print("Total Hits: " + str(hit_count))
        # Prompt user to play again or exit
        play_again = input("Do you want to play again?  "
                           "yes or no): ").lower().strip()
