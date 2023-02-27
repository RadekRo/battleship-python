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
        case _: 
            message = "Something went wrong :( Sorry! Please contact our team for support!"
    return message
