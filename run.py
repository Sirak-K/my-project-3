from random import randint


# Creates a 2D list: GUESSES (ship locations)
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]

# Creates a 2D list: HITS & MISSES
GUESS_BOARD = [[" "] * 8 for i in range(8)]
hit_count = 0

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
        
        while board[ship_row][ship_column] == "H":
            
            ship_row, ship_column = get_board_coordinates()
        
        board[ship_row][ship_column] = "H"



def get_board_coordinates() -> tuple:
    """
    Prompts the user to input the coordinates of a ship on the game board.

    Returns:S
    - a tuple containing the row and column indices of the ship.
    """

    # ROW
    row = input("Choose ROW 1-8: \n").upper().strip()
    print("You chose ROW: %s" % row)
    while row not in "12345678" or row == "":
        print('Please select a valid ROW')
        row = input("Choose ROW 1-8: \n").upper().strip()

    # COLUMN
    column = input("Choose COLUMN A-H: \n").upper().strip()
    print("You chose COLUMN: %s" % column)
    while column not in "ABCDEFGH" or column == "":
        print('Please select a valid COLUMN')
        column = input("Choose COLUMN A-H: \n").upper().strip()

    return int(row) - 1, board_coordinates[column]



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



if __name__ == "__main__":
    
    create_ship(HIDDEN_BOARD)
    
    turns_left = 3
    
    while turns_left > 0:
        
        print('Guess a battleship location')
        
        show_board(GUESS_BOARD)
        show_board(HIDDEN_BOARD)
        
        row, column = get_board_coordinates()
        
        if GUESS_BOARD[row][column] == "H" or GUESS_BOARD[row][column] == "M":
            print("This coordinate has already been targeted. Choose another!")
    
        

        elif HIDDEN_BOARD[row][column] == "H":
            print("HIT!")
            GUESS_BOARD[row][column] = "H"
            turns_left -= 1
        
        else:
            print("MISS!")
            GUESS_BOARD[row][column] = "M" # display "M" for missed hit
            turns_left -= 1

        if hit_tracker(GUESS_BOARD) == 5:
            print("You win!")
            break
        
        # PRINT THE NUMBER of turns remaining
        print("You have " + str(turns_left) + " turns left")
        
        # IF THE USER has run out of turns, print a failure message and exit the loop.
        if turns_left == 0:
            print("You ran out of turns")
            # PRINT FINAL SCORE
            print("Total Hits: " + str(hit_count))
