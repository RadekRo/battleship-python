import string

# player_one = {'A1': 'X', 'A2': '~', 'A3': '~', 'A4': '~', 'A5': '~', 'A6': '~', 'A7': '~', 'A8': '~', 'A9': '~', 'A10': '~', 'B1': 'X', 'B2': '~', 'B3': '~', 'B4': '~', 'B5': '~', 'B6': '~', 'B7': '~', 'B8': '~', 'B9': '~', 'B10': '~', 'C1': '~', 'C2': '~', 'C3': '~', 'C4': '~', 'C5': '~', 'C6': '~', 'C7': '~', 'C8': '~', 'C9': '~', 'C10': '~', 'D1': '~', 'D2': '~', 'D3': '~', 'D4': '~', 'D5': '~', 'D6': '~', 'D7': '~', 'D8': '~', 'D9': '~', 'D10': '~', 'E1': '~', 'E2': '~', 'E3': '~', 'E4': '~', 'E5': '~', 'E6': '~', 'E7': '~', 'E8': '~', 'E9': '~', 'E10': '~', 'F1': '~', 'F2': '~', 'F3': '~', 'F4': '~', 'F5': '~', 'F6': '~', 'F7': 
#'~', 'F8': '~', 'F9': 'X', 'F10': 'X', 'G1': '~', 'G2': '~', 'G3': '~', 'G4': '~', 'G5': '~', 'G6': '~', 'G7': '~', 'G8': '~', 'G9': '~', 'G10': '~', 'H1': '~', 'H2': '~', 'H3': '~', 'H4': '~', 'H5': '~', 'H6': '~', 'H7': '~', 'H8': '~', 'H9': '~', 'H10': '~', 'I1': '~', 'I2': '~', 'I3': '~', 'I4': '~', 'I5': '~', 'I6': '~', 'I7': '~', 'I8': '~', 'I9': '~', 'I10': '~', 'J1': '~', 'J2': '~', 'J3': '~', 'J4': '~', 'J5': '~', 'J6': '~', 'J7': '~', 'J8': '~', 'J9': '~', 
#'J10': '~'}

def check_surrounding(board, coordinate, width, height):

  alphabet = string.ascii_uppercase
  left, right, up, down = [False] * 4
  
  if int(coordinate[1:]) > 1:
    left = coordinate[0] + str(int(coordinate[1:]) - 1) 
    left = check_sail_presence(board, left)
    
  if int(coordinate[1:]) < width:
    right = coordinate[0] + str(int(coordinate[1:]) + 1) 
    right = check_sail_presence(board, right)

  if alphabet.index(coordinate[0]) > 0:
    up = alphabet[alphabet.index(coordinate[0]) - 1] + coordinate[1:]  
    up = check_sail_presence(board, up)
    
  if alphabet.index(coordinate[0]) < height:
    down = alphabet[alphabet.index(coordinate[0]) + 1] + coordinate[1:]
    down = check_sail_presence(board, down)

  return [left, right, up, down]

def block_surrounding_fields(board, coordinates):
  for field in coordinates:
      if field != "X" and field != False:
        board[field] = "."
  return board

def place_ship_on_board(board, coordinates):
  for coord in coordinates:
    board[coord] = "X"
    blocked_fields = check_surrounding(board, coord, BOARD_WIDTH, BOARD_HEIGHT)
    board = block_surrounding_fields(board, blocked_fields)
  return board

def get_empty_board(size):
    empty_board = {}
    for row in range(0, size):
        letter = string.ascii_uppercase[row]
        for column in range(0, size):
            coordination = letter + str(column + 1)
            empty_board[coordination] = "~"
    return empty_board

def get_board_header(size):
    board_row = "   "
    for row in range(1, size + 1):
        if row < 10:
            board_row += f" {row} "
        else:
            board_row += f"{row}"
    board_row += get_new_line()
    return board_row

def get_board_rows(board, size):
    board_rows = ""
    for row in range(0, size):
        current_row = string.ascii_uppercase[row]
        board_rows += f" {current_row} "
        for col in range(1, size + 1):
            board_rows += f" {board[current_row + str(col)]} "
        board_rows += get_new_line()
    return board_rows

def get_new_line():
    return "\n"

def display_board(board, size):
    board_header = get_board_header(size)
    board_rows = get_board_rows(board, size)
    board = board_header + board_rows
    print(board)

#display_board(player_one, 10)
