import random, string, time

alphabet = string.ascii_uppercase
alphabet_dict = dict()
for i in range(len(alphabet)):
    alphabet_dict[alphabet[i]] = i+1

def sunk_ship(board, coordinate, board_size):
    
    ship_sunk = False
    while ship_sunk == False:
        board[coordinate] = "S"
        letters_range = string.ascii_uppercase[:board_size]
        checklist = []
        hit = 0

        checklist.append(coordinate[0] + str(int(coordinate[1:]) - 1)) if int(coordinate[1:]) - 1 > 0 else False
        checklist.append(coordinate[0] + str(int(coordinate[1:]) + 1)) if int(coordinate[1:]) + 1 < board_size else False
        checklist.append(chr(ord(coordinate[0]) - 1) + coordinate[1:]) if chr(ord(coordinate[0]) - 1) in letters_range else False
        checklist.append(chr(ord(coordinate[0]) + 1) + coordinate[1:]) if chr(ord(coordinate[0]) + 1) in letters_range else False
        for field in checklist:
            if board[field] == "H":
                coordinate = field
                hit = 1
        ship_sunk = True if hit == 0 else False


                
                    
        



def check_if_ship_is_sunk(board, coordinate, board_size):
    letters_range = string.ascii_uppercase[:board_size]
    sail_check_left = coordinate[0] + str(int(coordinate[1:]) - 1) if int(coordinate[1:]) - 1 > 0 else False
    sail_check_right = coordinate[0] + str(int(coordinate[1:]) + 1) if int(coordinate[1:]) + 1 < board_size else False
    sail_check_up = chr(ord(coordinate[0]) - 1) + coordinate[1:] if chr(ord(coordinate[0]) - 1) in letters_range else False
    sail_check_down = chr(ord(coordinate[0]) + 1) + coordinate[1:] if chr(ord(coordinate[0]) + 1) in letters_range else False
    
    sail_check_list = [sail_check_left, sail_check_right, sail_check_up, sail_check_down]
    checklist = []
    for sail in sail_check_list:
        if sail != False:
            checklist.append(sail) if board[sail] == "X" else None
    return False if len(checklist) > 0 else True
            

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

def get_ai_random_ship_coordinates(board):
    # TODO: implement
    pass

def get_human_shot_coordinates(board, board_size):
    letters_range = string.ascii_uppercase[:board_size]
    human_coordinates = ""
    while human_coordinates == "":
        coordinates = input("Enter shot's coordinations (A1, B2..) \u2022 ").upper()
        
        if coordinates[0] not in alphabet_dict or not coordinates[1:].isdigit():
            print("Invalid coordinates! Try again.")
            continue

        if coordinates[0] not in letters_range or int(coordinates[1:]) > board_size: 
            print("Coordinates out of range! Try again.")
            continue
    
        if board[str(coordinates)] != "~" and board[str(coordinates)] != "X":
            print("You've allready shot there! You loose your turn!")
            time.sleep(1.6)
            human_coordinates = "double_shot"
        human_coordinates = coordinates

    return str(human_coordinates)

def get_ai_random_shot_coordinates(board):
    # TODO: implement
    pass

#     while True:
#         row = random.randint(1, len(board))
#         col = random.randint(1, len(board[0]))
#         if board[row-1][col-1] == "~":
#             return alphabet[row-1] + str(col)
