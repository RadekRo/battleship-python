from board import get_empty_board, display_board
# from coordinates import <nazwy funkcji>
from menu import menu

HUMAN_VS_HUMAN = 1
BOARD_SIZE = 5

def get_ship_base(size):
    three_sails = int(size * 0.2)
    two_sails = int((size - three_sails) * 0.4)
    one_sail = size - two_sails - three_sails
    return [three_sails, two_sails, one_sail]

def positioning_phase():
    board = get_empty_board(BOARD_SIZE)
    ship_quantity = get_ship_base(BOARD_SIZE)
    while
    display_board(board, BOARD_SIZE)


def main():
    # gameplay function
    game_mode = menu()
    player_one = positioning_phase()
    player_two = positioning_phase()
    #while game_mode == "active":
    # pass   
#main()
print(get_ship_base(5))