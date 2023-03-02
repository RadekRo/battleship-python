from board import get_empty_board, display_board
# from coordinates import <nazwy funkcji>
from menu import menu
from common import clear

HUMAN_VS_HUMAN = 1
BOARD_SIZE = 5

def get_ship_base(size):
    ships_base = list()
    three_sails = [3] * int(size * 0.2)
    two_sails = [2] * int((size - len(three_sails)) * 0.4)
    one_sail = [1] * (size - len(two_sails) - len(three_sails))
    ships_base = three_sails + two_sails + one_sail
    return ships_base

def positioning_phase(player):
    board = get_empty_board(BOARD_SIZE)
    ship_quantity = get_ship_base(BOARD_SIZE)
    clear()
    input(f"Press any key to deploying phase of PLAYER {player}!")
    while len(ship_quantity) > 0:
        clear()
        print(f"SHIP POSITIONING. PLAYER {player}.\n")
        display_board(board, BOARD_SIZE)
        current_ship = ship_quantity[0]
        print(f"Current ship: {current_ship} sail(s)")
        ship = input(f"Player {player} enter coordinates of your ship \u2022 ")
        del ship_quantity[0]
    clear()
    input(f"Press any key to proceed to PLAYER {player + 1}...")

def main():
    # gameplay function
    game_mode = menu()
    if game_mode == "active":
        player_one = positioning_phase(1)
        player_two = positioning_phase(2)
        #while game_mode == "active":
        # pass   
main()