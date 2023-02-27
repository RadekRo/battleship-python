import os

def clear():
    if (os.name == "posix"):
        os.system("clear")
    else:
        os.system("cls")

def get_message(string):
    message = ""
    match string:
        case "wrong-entry-in-menu":
            message = "## WRONG ENTRY! ## YOU MUST PROVIDE A NUMBER BETWEEN 1 AND 3!"
        case "exit-game":
            message = "You've quitted the game. Thanks for playing Battleship!"
        case "manual":
            message = """GAME MANUAL:
Two players sets their ships on the game board. 
After that both trying to guess where are the 
opponent's ships by providing board coordinations 
for a shot.Each shot might be a miss or a hit 
in enemy ship.Player which destroyes all 
the opposite ships - wins.
Good luck!    
--------------------------------------------------------------"""
        case _: 
            message = "Something went wrong :( Sorry! Please contact our team for support!"
    return message
