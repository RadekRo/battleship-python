import random

# create a dictionary with letters of the alphabet as keys and their corresponding indices as values
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_dict = {}
for i in range(len(alphabet)):
    alphabet_dict[alphabet[i]] = i+1

# function to get human player's ship coordinates
def get_human_ship_coordinates(board):
    while True:
        coordinates = input("Enter the coordinates of your ship: ")
        if coordinates[0].upper() not in alphabet_dict or not coordinates[1:].isdigit():
            print("Invalid coordinates! Try again.")
            continue
        row = alphabet_dict[coordinates[0].upper()]
        col = int(coordinates[1:])
        if row < 1 or row > len(board) or col < 1 or col > len(board[0]):
            print("Coordinates out of range! Try again.")
            continue
        if board[row-1][col-1] != "~":
            print("There's already a ship there! Try again.")
            continue
        return [coordinates]

# function to get random ship coordinates for AI player
def get_ai_random_ship_coordinates(board):
    # TODO: implement
    pass

# function to get human player's shot coordinates
def get_human_shot_coordinates(board):
    while True:
        coordinates = input("Enter the coordinates of your shot: ")
        if coordinates[0].upper() not in alphabet_dict or not coordinates[1:].isdigit():
            print("Invalid coordinates! Try again.")
            continue
        row = alphabet_dict[coordinates[0].upper()]
        col = int(coordinates[1:])
        if row < 1 or row > len(board) or col < 1 or col > len(board[0]):
            print("Coordinates out of range! Try again.")
            continue
        if board[row-1][col-1] != "~":
            print("You've already shot there! Try again.")
            continue
        return coordinates

# function to get random shot coordinates for AI player
def get_ai_random_shot_coordinates(board):
    while True:
        row = random.randint(1, len(board))
        col = random.randint(1, len(board[0]))
        if board[row-1][col-1] == "~":
            return alphabet[row-1] + str(col)
