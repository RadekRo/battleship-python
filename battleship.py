from board import get_empty_board, display_board
# from coordinates import <nazwy funkcji>
from menu import menu

HUMAN_VS_HUMAN = 1
BOARD_SIZE = 5

def positioning_phase():
    board = get_empty_board(BOARD_SIZE)
    print(board)

def main():
    # gameplay function
    game_mode = menu()
    player_one = positioning_phase()
    player_two = positioning_phase()
    #while game_mode == "active":
    # pass   
main()