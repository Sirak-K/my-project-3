from random import randint

# Creates a 2D list: GUESSES (ship locations)
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]

# Creates a 2D list: HITS & MISSES
GUESS_BOARD = [[" "] * 8 for i in range(8)]


def show_board(board: list) -> None:
    """
    Prints the game board to the console.

    Parameters:
    - board: a 2D list representing the game board.

    """
     
    # PRINT A HEADER
    print("  A B C D E F G H")
    
    # PRINT A HORIZONTAL LINE
    print("  +-+-+-+-+-+-+-+")
    
    current_row_number = 1
    
    # ITERATE
    for row in board:
        
        print("%d|%s|" % (current_row_number, "|".join(row)))
        
        current_row_number += 1


# BOARD COORDINATES
board_coordinates = {
    'A': 0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7
}


def create_ship(board: list) -> None: 
    """
    Randomly places 5 ships on the game board.

    Parameters:
    - board: a 2D list representing the game board.
     """

    for ship in range(5):
        print("Creating ship %d" % (ship+1))
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        
        while board[ship_row][ship_column] == "X":
            
            ship_row, ship_column = get_board_coordinates()
        
        board[ship_row][ship_column] = "X"



def get_board_coordinates() -> tuple:
    """
    Prompts the user to input the coordinates of a ship on the game board.

    Returns:
    - a tuple containing the row and column indices of the ship.
    """

    row = input("Enter row: ").upper()
    
    while row not in "12345678":
        print('Please select a valid row')
        row = input("Enter row: ").upper()
    
    column = input("Enter column: ").upper()
    
    while column not in "ABCDEFGH":
        print('Please select a valid column')
        column = input("Enter column: ").upper()
    
    return int(row) - 1, board_coordinates[column]


def hit_tracker(board: list) -> int:
    """
    Returns the number of hits on the guess board.

    Parameters:
    - board: a 2D list representing the guess board.

    Returns:
    - an integer representing the number of "X" characters on the board.
    """

    hit_count = 0

    for row in board:

        for column in row:

            if column == "X":
                hit_count += 1

    return hit_count




if __name__ == "__main__":
    
    create_ship(HIDDEN_BOARD)
    
    turns_left = 10
    
    while turns_left > 0:
        
        print('Guess a battleship location')
        
        show_board(GUESS_BOARD)
        
        row, column = get_board_coordinates()
        
        if GUESS_BOARD[row][column] == "-":
            print("You guessed that one already.")
        
        # IF THE GUESSED position on the hidden board contains an "X" (indicating a hit),
        # PRINT A SUCCESS message and update the guess board to display an "X".
        # THEN, DECREMENT the number of turns remaining.
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit")
            GUESS_BOARD[row][column] = "X"
            turns_left -= 1
        
        # IF THE GUESSED position on the hidden board does not contain an "X" (indicating a miss),
        # PRINT A FAILURE message and update the guess board to display a "-".
        # THEN, DECREMENT the number of turns remaining.
        else:
            print("MISS!")
            GUESS_BOARD[row][column] = "M" # display "M" for missed hit
            turns_left -= 1

        # IF THE USER has sunk all 5 ships, print a victory message and exit the loop.
        if hit_tracker(GUESS_BOARD) == 5:
            print("You win!")
            break
        
        # PRINT THE NUMBER of turns remaining
        print("You have " + str(turns_left) + " turns left")
        
        # IF THE USER has run out of turns, print a failure message and exit the loop.
        if turns_left == 0:
            print("You ran out of turns")
