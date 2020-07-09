import sys
import cmd
import os


def title_screen_selections():
    option = input("> ")
    option = option.lower().strip()
    if option.lower().strip() == "play":
        start_game()
    elif option.lower().strip() == "help":
        help_menu()
    else:
        sys.exit()
    while option.lower().strip() not in ["play", "help", "quit"]:
        print("please enter a valid command")
        if option.lower().strip() == "play":
            start_game()
        elif option.lower().strip() == "help":
            help_menu()
        else:
            sys.exit()


def title_screen():
    os.system("clear")
    print("####################################")
    print("#Welcome to the treasure adventure!#")
    print("####################################")
    print("              ~ Play ~              ")
    print("              ~ Help ~              ")
    print("              ~ Quit ~              ")
    title_screen_selections()


def help_menu():
    print("####################################")
    print("#Welcome to the treasure adventure!#")
    print("####################################")
    print("       Use n, s, e, w to move       ")
    print("   Type your commands to do them!   ")
    print("             Good luck              ")
    title_screen_selections()


# def start_game():
