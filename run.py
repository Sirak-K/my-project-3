# Great! These are all good optimizations to consider. Here's a summary of the optimizations with their new names according to the Karis-4 methodology:
# Opt-1: Remove unnecessary variables.
# Opt-2: Use list comprehensions to create the boards.
# Opt-3: Use elif instead of if for multiple conditions in the get_board_coordinates() function.
# Opt-4: Use format() instead of concatenation in the show_board() function.
# Opt-5: Avoid unnecessary function calls by combining show_board() calls in the main loop.
# Opt-6: Simplify the create_ship() function by using random.sample().
# Opt-7: Avoid unnecessary copying of lists in the reset_game_state() function.
# Opt-8: Simplify the setup_game() function by removing the board_size parameter and using a dictionary to map user input to board sizes.


from random import sample

# LIST: GUESSES
HIDDEN_BOARD_small = [[" "] * 4] * 4
HIDDEN_BOARD_medium = [[" "] * 6] * 6
HIDDEN_BOARD_large = [[" "] * 8] * 8

# LIST: HITS & MISSES
GUESS_BOARD_small = [[" "] * 4] * 4
GUESS_BOARD_medium = [[" "] * 6] * 6
GUESS_BOARD_large = [[" "] * 8] * 8

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
    print(" +{0}".format("-+" * board_scale))

    # Use a list comprehension to generate the row strings
    for i, row in enumerate(board):
        print("{0}|{1}|".format(i + 1, '|'.join(row)))

    # PRINT A HORIZONTAL LINE
    print(" +{0}".format("-+" * board_scale))

def show_boards(guess_board, hidden_board):
    print("Guess Board:")
    show_board(guess_board)
    print("\nHidden Board:")
    show_board(hidden_board)

def create_ship(board, board_size) -> None:
    """
    Randomly places 5 ships on the game board.

    Parameters:
    - board: a 2D list representing the game board.
    - board_size: a string representing the board size ("s", "m", or "l").
    """
    board_scale_x = len(board[0])
    board_scale_y = len(board)

    print("Creating Ships ", end="")
    
    # Generate a list of all possible coordinates on the board
    all_coords = [(row, col) for row in range(board_scale_y) for col in range(board_scale_x)]

    for idx, (ship_row, ship_column) in enumerate(sample(all_coords, NUM_SHIPS), start=1):
        if idx == NUM_SHIPS:
            print(idx)
        else:
            print(idx, end="-")
            
        board[ship_row][ship_column] = "S"

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

def reset_game_state(board_size):
    """
    Resets the game state for a new game by
    initializing necessary variables
    and clearing the hidden and guess boards.

    Parameters:
    - board_size: a string representing the board size
    ("s", "m", or "l").

    Returns:
    - a tuple containing the hidden_board, guess_board,
    TURNS_LEFT, and hit_count variables.
    """
    board_scale = len(BOARD_SIZES_DICT[board_size]["HIDDEN_BOARD"])

    # Create new hidden_board and guess_board using a list comprehension
    hidden_board = [[" "] * board_scale for _ in range(board_scale)]
    guess_board = [[" "] * board_scale for _ in range(board_scale)]
    
    TURNS_LEFT = 3
    hit_count = 0

    return hidden_board, guess_board, TURNS_LEFT, hit_count

def setup_game():
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

    # Reset hidden_board and guess_board using a list comprehension
    hidden_board, guess_board, TURNS_LEFT, _ = reset_game_state(board_size)

    # Randomly place 5 ships on the hidden board
    create_ship(hidden_board, board_size)

    return hidden_board, guess_board, TURNS_LEFT

if __name__ == "__main__":
    play_again = "yes"
    while play_again.lower() == "yes":

        hidden_board, guess_board, TURNS_LEFT = setup_game()
        hit_count = 0

        while TURNS_LEFT > 0:
            show_boards(guess_board, hidden_board)
            
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