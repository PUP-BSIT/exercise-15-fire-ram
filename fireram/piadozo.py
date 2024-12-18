import random
import os

UNSET_OPTION = -1
EXIT_OPTION = 0

class CardGame:
    list_of_account = []
    def __init__(self, name, pin, age, balance_user):
        self.name = name
        self.pin = pin
        self.age = age
        self.balance_user = balance_user

    def create_account (self):
        num_account = int(input("Enter the number of account: "))
        for num in range (num_account):
            print(f"Account number {num}")
            user_name = str(input("Enter your username: "))
            user_pin = str(input("Enter your user pin: "))
            user_age = int(input("Enter your age: "))
            user_balance = 0
            account = CardGame(user_name, user_pin, user_age, user_balance)
            CardGame.list_of_account.append(account)

    def show_information(self):
            print (f"Your name is: {self.name}")
            print (f"Your user pin is: {self.pin}")
            print (f"Your age is: {self.age}")
            print (f"Your current balance is: {self.balance_user}")
    
    def show_information_display ():
        if not CardGame.list_of_account:
            print ("No accounts found")
            return
    
        account_finder = int(input("Enter a number to find your account "
                                   + "start from 0: "))
        CardGame.list_of_account[account_finder].show_information()

    def get_list_of_registered_account ():
        if not CardGame.list_of_account:
            print ("No account")
            return

        print ("List of account")
        for account in CardGame.list_of_account:
            account.show_information()
            print ("-" * 30)

    def top_up_balance (self):
        if self.age <= 17:
            print ("Age restricted")
            return

        print ("Please input a balance")
        user_input_balance = int(input("Top up : "))
        self.balance_user += user_input_balance
        print (f"Your total balance is: {self.balance_user}")
    
    def top_up_balance_display ():
        if not CardGame.list_of_account:
            print ("No accounts found")
            return
        
        choice_account = int(input("Enter your number of account: "))
        CardGame.list_of_account[choice_account].top_up_balance()

    def show_banker_show_player(self, place_bet, money_bet, banker, player):
        if place_bet == "Banker":
            if banker > player:
                print("Congratulations you win")
                self.balance_user += money_bet
            elif banker == player:
                print("Print it's draw")
                self.balance_user == self.balance_user
            else: 
                print ("Sorry you lose")
                self.balance_user -= money_bet

        elif place_bet == "Player":
            if player > banker:
                print ("Congratulations you win")
                self.balance_user += money_bet
            elif banker == player:
                print("Print it's draw")
                self.balance_user == self.balance_user
            else:
                print ("You lose")
                self.balance_user -= money_bet
        else:
            print("Balance is not enough")
            return

    def play_card_game(self):
        money_bet = int(input("Enter your bet: "))
        if self.balance_user < money_bet:
            print ("Not enough balance")
            return 
       
        print ("Card game Baccarat")
        place_bet = input("Placebet (Banker/Player): ")
        card_one = random.randint(1, 9)
        card_two = random.randint(1,9)
        card_three = random.randint(1,9)
        card_four = random.randint(1,9)
        banker = (card_one + card_two) % 10
        player = (card_three + card_four) % 10
        print (f"The result of banker: {banker}")
        print (f"The result of player: {player}")
        self.show_banker_show_player(place_bet, money_bet, banker, player)

    def play_card_game_display ():
        if not CardGame.list_of_account:
            print ("No accounts found")
            return
        
        choice_account = int(input("Enter your number of account: "))
        CardGame.list_of_account[choice_account].play_card_game()
            
    def menu():
        os.system("cls")
        main_choice = UNSET_OPTION
        while main_choice != EXIT_OPTION:
            main_choice = CardGame.display_choice()
            CardGame.process_choice(main_choice)

    def display_choice ():
        os.system("cls")
        print ("1. Create account")
        print ("2. Information")
        print ("3. Registered account")
        print ("4. Input a balance")
        print ("5. Card game")
        print ("0. Exit")

        return int(input("Enter your choice: "))

    def process_choice (main_choice):
        match main_choice:
            case 1:
                os.system("cls")
                game = CardGame("", "", 0, 0)
                game.create_account()
                input()
            case 2:
                os.system("cls")
                CardGame.show_information_display()
                input()
            case 3:
                os.system("cls")
                CardGame.get_list_of_registered_account()
                input()
            case 4:
                os.system("cls")
                CardGame.top_up_balance_display()
                input()
            case 5:
                os.system("cls")
                CardGame.play_card_game_display()
                input()
            case _:
                return