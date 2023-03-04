from board import get_empty_board, display_board, place_ship_on_board, leave_only_ships_on_board, display_double_board, get_board_legend
from coordinates import get_human_ship_coordinates, get_human_shot_coordinates, check_if_ship_is_sunk
from menu import menu
from common import clear
from graphics import get_menu_header
import time

HUMAN_VS_HUMAN = 1
BOARD_SIZE = 5

def get_ship_base(size):
    ships_base = list()
    three_sails = [3] * int(size * 0.2)
    two_sails = [2] * int((size - len(three_sails)) * 0.4)
    one_sail = [1] * (size - len(two_sails) - len(three_sails))
    ships_base = three_sails + two_sails + one_sail
    return ships_base

def pause_game(player, phase):
    if phase == "deploy":
        input(f"Press [ENTER] for deploying phase of PLAYER {player}...")
    elif phase == "shoot":
        input(f"Press [ENTER] for shooting phase of the game!")

def positioning_phase(player):
    board = get_empty_board(BOARD_SIZE)
    ship_quantity = get_ship_base(BOARD_SIZE)
    clear()
    get_menu_header()
    pause_game(player, "deploy")
    while len(ship_quantity) > 0:
        current_ship = ship_quantity[0]
        clear()
        get_menu_header()
        print(f"SHIP POSITIONING. PLAYER {player}.\n")
        display_board(board, BOARD_SIZE)
        print(f"Remaining ships: {len(ship_quantity)}.")
        print(f"Current ship: {current_ship} sail(s).")
        coords = get_human_ship_coordinates(board, current_ship, BOARD_SIZE)
        if len(coords) > 0:
            place_ship_on_board(board, coords, BOARD_SIZE)
            del ship_quantity[0]
    board = leave_only_ships_on_board(board)
    return board

def shooting_phase(first_board, second_board, size):
    
    winner = ""
    turn = 1
    clear()
    get_menu_header()
    pause_game(..., "shoot")
    
    while winner == "":
        clear()
        get_menu_header()
        display_double_board(second_board, first_board, size)
        
        if turn % 2 != 0:
            current_board = second_board
            print("PLAYER 1 TURN:")
            print(get_board_legend())
            shot = get_human_shot_coordinates(current_board, BOARD_SIZE)
        else:
            current_board = first_board
            print("PLAYER 2 TURN:")
            print(get_board_legend())
            shot = get_human_shot_coordinates(current_board, BOARD_SIZE)
        
        turn += 1

        if shot =="double_shot":
            continue
        else:
            if current_board[shot] != "X":
                print("You've missed!")
                current_board[shot] = "M"
                time.sleep(1.6)
            else:
                print("You've hit a ship!")
                current_board[shot] = "H"
                sunk = check_if_ship_is_sunk(current_board, shot, BOARD_SIZE)
                if sunk == True:
                    print("SHIP SUNK, big splash!") 
                time.sleep(1.6)

def main():
    clear()
    game_mode = menu()
    if game_mode == "active":
        player_one = positioning_phase(1)
        player_two = positioning_phase(2)
        clear()
        shooting_phase(player_one, player_two, BOARD_SIZE)
           
main()