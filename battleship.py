from board import get_empty_board, display_board, place_ship_on_board
from coordinates import get_human_ship_coordinates
from menu import menu
from common import clear
from graphics import get_menu_header

HUMAN_VS_HUMAN = 1
BOARD_SIZE = 5

def get_ship_base(size):
    ships_base = list()
    three_sails = [3] * int(size * 0.2)
    two_sails = [2] * int((size - len(three_sails)) * 0.4)
    one_sail = [1] * (size - len(two_sails) - len(three_sails))
    ships_base = three_sails + two_sails + one_sail
    return ships_base

def pause_game(player):
    input(f"Press [ENTER] for deploying phase of PLAYER {player}...")

def positioning_phase(player):
    board = get_empty_board(BOARD_SIZE)
    ship_quantity = get_ship_base(BOARD_SIZE)
    clear()
    get_menu_header()
    pause_game(player)
    while len(ship_quantity) > 0:
        clear()
        get_menu_header()
        print(f"SHIP POSITIONING. PLAYER {player}.\n")
        display_board(board, BOARD_SIZE)
        current_ship = ship_quantity[0]
        print(f"Remaining ships: {len(ship_quantity)}.")
        print(f"Current ship: {current_ship} sail(s).")
        #ship = input(f"Player {player} enter coordinates of your ship  ")
        coords = get_human_ship_coordinates(board, current_ship, BOARD_SIZE)
        if len(coords) > 0:
            place_ship_on_board(board, coords, BOARD_SIZE)
            del ship_quantity[0]
    clear()

def main():
    # gameplay function
    clear()
    game_mode = menu()
    if game_mode == "active":
        player_one = positioning_phase(1)
        player_two = positioning_phase(2)
        #while game_mode == "active":
        # pass   
main()