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
    "small": {"HIDDEN_BOARD": HIDDEN_BOARD_small, "GUESS_BOARD": GUESS_BOARD_small},
    "medium": {"HIDDEN_BOARD": HIDDEN_BOARD_medium, "GUESS_BOARD": GUESS_BOARD_medium},
    "large": {"HIDDEN_BOARD": HIDDEN_BOARD_large, "GUESS_BOARD": GUESS_BOARD_large},
}

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
    column_headers = "  " + " ".join(chr(i) for i in range(65, 65 + board_scale))
    print(column_headers)

    # PRINT A HORIZONTAL LINE
    print(" +" + "-+" * board_scale)

    current_row_number = 1

    # ITERATE
    for row in board:

        print("%d|%s|" % (current_row_number, "|".join(row)))

        current_row_number += 1


# BOARD COORDINATES
board_coordinates = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}


def create_ship(board: list, board_scale: str) -> None:
    """
    Randomly places 5 ships on the game board.

    Parameters:
    - board: a 2D list representing the game board.
    - board_scale: a string representing the board size ("small", "medium", or "large").
    """

    # Calculate the size of the board
    # VARIABLES DEFINED
    if board_scale == "small":
        board_size_x = 4
        board_size_y = 4
    elif board_scale == "medium":
        board_size_x = 6
        board_size_y = 6
    elif board_scale == "large":
        board_size_x = 8
        board_size_y = 8
    else:
        raise ValueError("Invalid board size. Please choose small, medium, or large.")

    for ship in range(5):
        print("Creating ship %d" % (ship + 1))
        ship_row, ship_column = randint(0, board_size_y - 1), randint(
            0, board_size_x - 1
        )

        while board[ship_row][ship_column] == "H":

            ship_row, ship_column = randint(0, board_size_y - 1), randint(
                0, board_size_x - 1
            )

        board[ship_row][ship_column] = "H"


def get_board_coordinates() -> tuple:
    """
    Prompts the user to input the coordinates of a ship on the game board.

    Returns:S
    - a tuple containing the row and column indices of the ship.
    """

    # ROW
    row = (
        input(
            "Choose ROW 1-{}: \n".format(
                len(BOARD_SIZES_DICT[BOARD_SIZES]["HIDDEN_BOARD"])
            )
        )
        .upper()
        .strip()
    )
    print("You chose ROW: %s" % row)
    while row not in [
        str(i) for i in range(1, len(BOARD_SIZES_DICT[BOARD_SIZES]["HIDDEN_BOARD"]) + 1)
    ]:
        print("Please select a valid ROW")
        row = (
            input(
                "Choose ROW 1-{}: \n".format(
                    len(BOARD_SIZES_DICT[BOARD_SIZES]["HIDDEN_BOARD"])
                )
            )
            .upper()
            .strip()
        )

    # COLUMN
    column = (
        input(
            "Choose COLUMN A-{}: \n".format(
                chr(64 + len(BOARD_SIZES_DICT[BOARD_SIZES]["HIDDEN_BOARD"][0]))
            )
        )
        .upper()
        .strip()
    )
    print("You chose COLUMN: %s" % column)
    while column not in [
        chr(i)
        for i in range(65, 65 + len(BOARD_SIZES_DICT[BOARD_SIZES]["HIDDEN_BOARD"][0]))
    ]:
        print("Please select a valid COLUMN")
        column = (
            input(
                "Choose COLUMN A-{}: \n".format(
                    chr(64 + len(BOARD_SIZES_DICT[BOARD_SIZES]["HIDDEN_BOARD"][0]))
                )
            )
            .upper()
            .strip()
        )

    return int(row) - 1, ord(column) - 65


def hit_tracker(board: list) -> int:
    """
    Returns the number of hits on the guess board and updates the hit_count variable.

    Parameters:
    - board: a 2D list representing the guess board.

    Returns:
    - an integer representing the number of "X" characters on the board.
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
    Resets the game state for a new game by initializing necessary variables and clearing the hidden and guess boards.

    Parameters:
    - board_sizes: a string representing the board size ("small", "medium", or "large").

    Returns:
    - a tuple containing the hidden_board, guess_board, turns_left, and hit_count variables.
    """
    hidden_board = BOARD_SIZES_DICT[board_sizes]["HIDDEN_BOARD"]
    guess_board = BOARD_SIZES_DICT[board_sizes]["GUESS_BOARD"]
    turns_left = 3
    hit_count = 0

    # Reset hidden_board and guess_board
    for row_idx, row in enumerate(hidden_board):
        for col_idx, _ in enumerate(row):
            hidden_board[row_idx][col_idx] = " "
            guess_board[row_idx][col_idx] = " "

    return hidden_board, guess_board, turns_left, hit_count


if __name__ == "__main__":
    play_again = "yes"
    while play_again.lower() == "yes":

        # Prompt user to choose board size
        BOARD_SIZES = (
            input("Choose board size (small, medium, or large): ").lower().strip()
        )

        # Initialize game variables
        HIDDEN_BOARD, GUESS_BOARD, turns_left, hit_count = reset_game_state(BOARD_SIZES)

        # Set board and guess boards based on chosen board size
        if BOARD_SIZES == "small":
            HIDDEN_BOARD = BOARD_SIZES_DICT["small"]["HIDDEN_BOARD"]
            GUESS_BOARD = BOARD_SIZES_DICT["small"]["GUESS_BOARD"]
        elif BOARD_SIZES == "medium":
            HIDDEN_BOARD = BOARD_SIZES_DICT["medium"]["HIDDEN_BOARD"]
            GUESS_BOARD = BOARD_SIZES_DICT["medium"]["GUESS_BOARD"]
        elif BOARD_SIZES == "large":
            HIDDEN_BOARD = BOARD_SIZES_DICT["large"]["HIDDEN_BOARD"]
            GUESS_BOARD = BOARD_SIZES_DICT["large"]["GUESS_BOARD"]

        else:
            print("Invalid board size. Please choose small, medium, or large.")
            exit()

        create_ship(HIDDEN_BOARD, BOARD_SIZES)

        turns_left = 3

        while turns_left > 0:

            print("Your turn! Guess a battleship location.")

            show_board(BOARD_SIZES_DICT[BOARD_SIZES]["GUESS_BOARD"])
            # show_board(BOARD_SIZES_DICT[BOARD_SIZES]["HIDDEN_BOARD"])

            row, column = get_board_coordinates()

            if GUESS_BOARD[row][column] == "H" or GUESS_BOARD[row][column] == "M":
                print("This coordinate has already been targeted. Choose another!")

            # If the guess matches a hidden ship, add 1 to hit_count and decrease turns_left
            elif HIDDEN_BOARD[row][column] == "H":
                print("HIT!")
                GUESS_BOARD[row][column] = "H"
                turns_left -= 1
            # If the guess doesn't match a hidden ship, decrease turns_left
            else:
                print("MISS!")
                GUESS_BOARD[row][column] = "M"  # display "M" for missed hit
                turns_left -= 1
            # If the player hits all 5 ships, end the game
            if hit_tracker(GUESS_BOARD) == 5:
                print("You win!")
                break

            # PRINT THE NUMBER of turns remaining
            print("You have " + str(turns_left) + " turns left.")

            # IF THE USER has run out of turns, print a failure message and exit the loop.
            if turns_left == 0:
                print("You ran out of turns")
                # PRINT FINAL SCORE
                print("Total Hits: " + str(hit_count))
        # Prompt user to play again or exit
        play_again = input("Do you want to play again? (yes or no): ").lower().strip()
