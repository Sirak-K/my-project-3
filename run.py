from random import randint


# Creates a 8x8 two-dimensional list: guesses (ship locations)
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]

# The >>     [" "] * 8     << creates a list of 8 space characters, 
# The >> for i in range(8) << repeats this process 8 times to create a list of 8 lists. 

# Creates a 8x8 two-dimensional list: hits and misses
GUESS_BOARD = [[" "] * 8 for i in range(8)]



# DEFINE A FUNCTION: called show_board that takes a single argument called board
# The row number is incremented by 1 with each iteration through the loop
def show_board(board):
    
    # PRINT A HEADER ROW with the column labels for the game board
    print("  A B C D E F G H")
    
    # PRINT A HORIZONTAL LINE to separate the header row from the game board
    print("  +-+-+-+-+-+-+-+")
    
    # INITIALIZE A ROW NUMBER variable to 1
    row_number = 1
    
    # ITERATE OVER EACH ROW in the board variable
    for row in board:
        # Combine the characters in the row with vertical bars to create a string representation of the row
        # and print the row number and string representation of the row with vertical bars
        print("%d|%s|" % (row_number, "|".join(row)))
        # Increment the row number variable by 1
        row_number += 1


# CREATE A DICTIONARY called game_grid that maps each letter from 'A' to 'H' to an integer value from 0 to 7
game_grid = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}


# -- F 1 # Implement a given algorithm as a computer program --------------------------------------------------------
# The function places 5 ships randomly on the board.
def ship_create(board):
    
    # LOOP 5 TIMES TO CREATE 5 SHIPS
    for ship in range(5):
        
        # GENERATE RANDOM ROW AND COLUMN INDICES FOR the ship
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        
        # CHECK IF THE CHOSEN POSITION ALREADY HAS A SHIP ON IT
        while board[ship_row][ship_column] == "X":
            
            # IF THE CHOSEN POSITION ALREADY HAS A SHIP ON IT, 
            # GENERATE NEW random row and column indices
            ship_row, ship_column = ship_location()
        
        # SET THE CHOSEN POSITION ON THE BOARD to contain a ship
        board[ship_row][ship_column] = "X"




# -- F 2 # Adapt and combine algorithms to solve a given problem --------------------------------------------------------
# This code defines a function ship_location that prompts 
# the user to input the location (row and column) of a ship on the board.
# This function prompts the user to enter a row and column for a ship location,
# and validates that the input is a valid row and column for the game board.
def ship_location():
    
    # PROMPT THE USER to enter a row for the ship
    row = input("Enter row: ").upper()
    
    # VALIDATE ROW INPUT is a valid row number for the game board
    while row not in "12345678":
        print('Please select a valid row')
        row = input("Enter row: ").upper()
    
    # PROMPT THE USER to enter a column for the ship
    column = input("Enter column: ").upper()
    
    # VALIDATE COLUMN INPUT is a valid column letter for the game board
    while column not in "ABCDEFGH":
        print('Please select a valid column')
        column = input("Enter column: ").upper()
    
    # CONVERT ROW COLUMN INPUTS to integer indices for the game board
    # (subtract 1 from the row number to account for zero-indexing)
    return int(row) - 1, game_grid[column]


# -- F 3 --------------------------------------------------------
# This code defines a function hits that takes a 2D-list as an argument.
# This function counts the number of "X" characters (representing hits) on the game board.
def hits(board):
    
    # INITIALIZE VARIABLE to 0
    count = 0
    
    # ITERATE OVER EACH ROW in the board
    for row in board:
        
        # ITERATE OVER EACH COLUMN in the row
        for column in row:
            
            # IF the current position contains an "X", 
            # INCREMENT THE VARIABLE
            if column == "X":
                count += 1
    
    # RETURN the final count of hits on the board
    return count



# Adequately use standard programming constructs: repetition, 
# selection, functions, composition, modules, aggregated data (arrays, lists, etc.)

# The following code block runs when the program is executed as a standalone script.
# The code creates 5 ships on the hidden board, and then prompts the user to guess the locations of the ships.
if __name__ == "__main__":
    
    # CREATE 5 SHIPS on the hidden board
    ship_create(HIDDEN_BOARD)
    
    # INITIALIZE THE NUMBER of turns to 10
    turns = 10
    
    # REPEAT THE GUESSING process until the user runs out of turns or sinks all 5 ships
    while turns > 0:
        
        # PRINT A MESSAGE prompting the user to guess a battleship location
        print('Guess a battleship location')
        
        # DISPLAY THE CURRENT state of the guess board to the user
        show_board(GUESS_BOARD)
        
        # PROMPT THE USER to enter a row and column for their guess
        row, column = ship_location()
        
        # IF THE GUESSED position on the guess board already contains a "-" (indicating a previous miss),
        
        # PRINT AN ERROR message and skip the rest of the loop.
        if GUESS_BOARD[row][column] == "-":
            print("You guessed that one already.")
        
        # IF THE GUESSED position on the hidden board contains an "X" (indicating a hit),
        # PRINT A SUCCESS message and update the guess board to display an "X".
        # THEN, DECREMENT the number of turns remaining.
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit")
            GUESS_BOARD[row][column] = "X"
            turns -= 1
        



        # IF THE GUESSED position on the hidden board does not contain an "X" (indicating a miss),
        # PRINT A FAILURE message and update the guess board to display a "-".
        # THEN, DECREMENT the number of turns remaining.
        else:
            print("MISS!")
            GUESS_BOARD[row][column] = "M" # display "M" for missed hit
            turns -= 1
        



        # IF THE USER has sunk all 5 ships, print a victory message and exit the loop.
        if hits(GUESS_BOARD) == 5:
            print("You win!")
            break
        
        # PRINT THE NUMBER of turns remaining
        print("You have " + str(turns) + " turns left")
        
        # IF THE USER has run out of turns, print a failure message and exit the loop.
        if turns == 0:
            print("You ran out of turns")
