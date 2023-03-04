import random, string, time

# create a dictionary with letters of the alphabet as keys and their corresponding indices as values
alphabet = string.ascii_uppercase
alphabet_dict = dict()
for i in range(len(alphabet)):
    alphabet_dict[alphabet[i]] = i+1

# function to get human player's ship coordinates
def get_human_ship_coordinates(board, ship, board_size):
    
    letters_range = list(string.ascii_uppercase[:board_size])
    ship_directions = ["H", "V"]
    human_ship_coordinates = list()
    check_length_range = int(ship - 1)

    while len(human_ship_coordinates) < 1:
        coordinates = input("Enter your ship starting position (A1, B2..) \u2022 ").upper()
        if ship > 1:
            direction = input("""Enter ship direction 
\033[93mH\033[0m for horizontal or \033[93mV\033[0m for vertical \u2022 """).upper()  
        else:
            direction = "H"
            
        if coordinates[0] not in alphabet_dict or not coordinates[1:].isdigit() or direction not in ship_directions:
            print("Invalid coordinates! Try again.")
            continue

        if chr(ord(coordinates[0]) + check_length_range) not in letters_range and direction == "V": 
            print("Coordinates out of range! Try again.")
            continue

        if int(coordinates[1:]) + check_length_range > board_size and direction == "H":
            print("Coordinates out of range! Try again.")
            continue

        for i in range(ship):
            if direction == "V":
                sail = chr(ord(coordinates[0]) + i) + str(int(coordinates[1:]))
            else: 
                sail = chr(ord(coordinates[0])) + str(int(coordinates[1:]) + i)
            human_ship_coordinates.append(sail)
        
        for sail in human_ship_coordinates:
            if board[sail] == "X":
                print("Invalid coordinates! There's already a ship there! Try again!")
                human_ship_coordinates = list()
                time.sleep(1.6)
                break
            elif board[sail] == ".":
                print("Invalid coordinates! To close to other ship! Try again!")
                human_ship_coordinates = list()
                time.sleep(1.6)
                break
        return human_ship_coordinates

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
