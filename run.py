# PROCESS #
# Step 1) Initializing the boards
# Step 2) Randomly placing the ships on the board
# Step 3) Asking the user for their guess
# Step 4) Checking if the guess is a hit or miss
# Step 5) Displaying the updated guess board
# Step 6) Checking if all the ships have been sunk
# Step 7) Printing messages for a hit or miss
# Step 8) Ending the game when all ships have been sunk

from random import randint

# Creates a 8x8 two-dimensional list: guesses (ship locations)
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
# Creates a 8x8 two-dimensional list: hits and misses
GUESS_BOARD = [[" "] * 8 for i in range(8)]

# The row number is incremented by 1 with each iteration through the loop
def show_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


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


# The function places 5 ships randomly on the board.
def ship_create(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = ship_location()
        board[ship_row][ship_column] = "X"

# This code defines a function ship_location that prompts 
# the user to input the location (row and column) of a ship on the board.
def ship_location():
    row = input("Enter row: ").upper()
    while row not in "12345678":
        print('Please select a valid row')
        row = input("Enter row: ").upper()
    column = input("Enter column: ").upper()
    while column not in "ABCDEFGH":
        print('Please select a valid column')
        column = input("Enter column: ").upper()
    return int(row) - 1, game_grid[column]

# This code defines a function hits that takes a 2D-list as an argument.
def hits(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


if __name__ == "__main__":
    ship_create(HIDDEN_BOARD)
    turns = 10
    while turns > 0:
        print('Guess a battleship location')
        show_board(GUESS_BOARD)
        row, column = ship_location()
        if GUESS_BOARD[row][column] == "-":
            print("You guessed that one already.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit")
            GUESS_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("MISS!")
            GUESS_BOARD[row][column] = "-"
            turns -= 1
        if  hits(GUESS_BOARD) == 5:
            print("You win!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You ran out of turns")