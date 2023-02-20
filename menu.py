def menu():
    print("1. Nowa gra")
    print("2. Instrukcja")
    print("3. Wyjdź")
    
    choice = input("Wybierz opcję: ")
    
    if choice == "1":
        start_game()
    elif choice == "2":
        print("Na jednej planszy gracz rysuje swoje statki")
        print("a na drugiej zaznacza nietrafione strzały w statki przeciwnika oraz oznaczenia trafionych okrętów.")
        print("statki mogą być ustawione w pionie lub poziomie wygrywa gracz który jako pierwszy zniszczy wszystkie statki")
        menu()
    elif choice == "3":
        exit()
    else:
        print("Nieprawidłowy wybór, spróbuj ponownie.")
        menu()

def start_game():
    print("kod gry") 
    menu()

menu()
