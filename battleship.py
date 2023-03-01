from board import get_empty_board, display_board
# from coordinates import <nazwy funkcji>
from menu import menu

HUMAN_VS_HUMAN = 1
BOARD_WIDTH = 10
BOARD_HEIGHT = 10

def positioning_phase():
    board = get_empty_board(BOARD_WIDTH, BOARD_HEIGHT)
    print(board)

def main():
    # gameplay function
    game_mode = menu()
    player_one = positioning_phase()
    player_two = positioning_phase()
    #while game_mode == "active":
    # pass   
main()