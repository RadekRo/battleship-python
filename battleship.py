from board import get_empty_board, display_board
# from coordinates import <nazwy funkcji>
from menu import menu

HUMAN_VS_HUMAN = 1
BOARD_WIDTH = 5
BOARD_HEIGHT = 5

def main():
    # gameplay function
    game_mode = menu()
    while game_mode == "active":
        break
main()