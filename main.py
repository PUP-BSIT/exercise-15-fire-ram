from fireram import piadozo, consultado
import os

UNSET_OPTION = " "
EXIT_OPTION = "0"

def menu():
    user_choice = UNSET_OPTION
    while user_choice != EXIT_OPTION:
        user_choice = display_choice()
        process_choice(user_choice)

def display_choice():
    os.system('cls')
    print("===============> Fire Ram <===============")
    print("1. Edriane O. Piadozo")
    print("2. Kirby G. Consultado")
    print("3. Gener A. Andaya Jr. ")
    print("4. Kevin Joseph V. Barcelos")
    print("5. Marc D. Veslino")
    print("0. Exit ")
    print("===============> <======> <===============")
    
    return input("Enter your choice: ")

def process_choice(user_choice):
    match user_choice:
        case '1':
            piadozo.CardGame.menu()
        case '2':
            consultado.Customer.menu()
        case '3':
            pass
        case '4':
            pass
        case '5':
            pass
        case '0':
            pass
        case _:
            input("Invalid input.")

menu()