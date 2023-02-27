# from board import <nazwy funkcji>
# from coordinates import <nazwy funkcji>
from menu import menu

HUMAN_VS_HUMAN = 1
HUMAN_VS_RANDOM_AI = 2

def main():
    # gameplay function
    game_mode = menu()
    while game_mode == "active":
        break

main()