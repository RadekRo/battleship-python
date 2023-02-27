import string

def get_empty_board(width, height):
    empty_board = {}
    for row in range(0, height):
        letter = string.ascii_uppercase[row]
        for column in range(0, width):
            coordination = letter + str(column + 1)
            empty_board[coordination] = "~"
    return empty_board

def display_board(board, width, height):
   # should return a graphic representation
   # of a dictionary board, using height/width
   # create and print board
