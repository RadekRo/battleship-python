import string

def get_empty_board(width, height):
    empty_board = {}
    for row in range(0, height):
        letter = string.ascii_uppercase[row]
        for column in range(0, width):
            coordination = letter + str(column + 1)
            empty_board[coordination] = "~"
    return empty_board
    
def display_board(board):

    player_one = input("Nick gracza \n• ")
    player_one = player_one.upper()
    print(" ")
    print("    1   2   3   4   5")
    print("  ","---+---+---+---+---")
    print("A", "|", board[0][0], "|", board[0][1], "|", board[0][2], "|", board[0][3], "|", board[0][4], "|")
    print("  ","---+---+---+---+---")
    print("B", "|", board[1][0], "|", board[1][1], "|", board[1][2], "|", board[0][3], "|", board[0][4], "|")
    print("  ","---+---+---+---+---")
    print("C", "|", board[2][0], "|", board[2][1], "|", board[2][2], "|", board[0][3], "|", board[0][4], "|")
    print("  ","---+---+---+---+---")
    print("D", "|", board[3][0], "|", board[3][1], "|", board[3][2], "|", board[0][3], "|", board[0][4], "|")
    print("  ","---+---+---+---+---")
    print("E", "|", board[4][0], "|", board[4][1], "|", board[4][2], "|", board[0][3], "|", board[0][4], "|")
    print("  ","---+---+---+---+---")

#empty_board = get_empty_board()
#print(empty_board)



#display_board(empty_board)