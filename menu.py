from common import clear, get_message
from graphics import get_menu_header

def get_user_entry():
  choice = int(input("CHOOSE AN OPTION \u2022 "))
  return choice

def user_entry_validation(user_entry):
  return user_entry == 1

def menu():
  
  user_entry = 0
  error_message = False
  show_manual = False

  while user_entry != 1:
    get_menu_header()
    print("""1. NEW GAME
2. MANUAL
3. QUIT
         """)
    if error_message == True:
      print(get_message("wrong-entry-in-menu"))

    if show_manual == True:
      print(get_message("manual"))

    try:
      user_entry = get_user_entry()
    except:
      error_message = True

    show_manual = True if user_entry == 2 else False

    if user_entry == 3:
      print(get_message("exit-game"))
      break
    
    if user_entry_validation(user_entry):
      return "active"
    else:
      error_message = True if user_entry != 2 else False

    clear()