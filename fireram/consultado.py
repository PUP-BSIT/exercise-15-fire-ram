from colorama import Fore
import os

UNSET_OPTION = '-1'
EXIT_OPTION = '0'

class Customer:
    def __init__(self, name, brand, model, price, date):
        self.name = name
        self.brand = brand
        self.model = model
        self.price = price
        self.date = date

    def display_name(self):
        if not self.name:
            print("\nNo input.")
            return
        
        print(f"\nThe name of the customer is "
              f"{Fore.CYAN + self.name + Fore.RESET}.")

    def display_car(self):
        if not self.brand or not self.model:
            print("\nIncomplete data.")
            return
        
        print(f"\nThe brand of car he bought is {Fore.CYAN + self.brand} "
              f"{self.model + Fore.RESET}.")

    def display_price(self):
        if not self.brand or not self.model or not self.price:
            print("\nIncomplete data.")
            return
        
        print(f"\nThe {Fore.CYAN + self.brand} {self.model + Fore.RESET}"
              f" was sold for {Fore.CYAN + self.price} PHP." + Fore.RESET)
        
    def display_date(self):
        if not self.date:
            print("\nNo input.")
            return
        
        print(f"\nThe car was purchased on "
              f"{Fore.CYAN + self.date + Fore.RESET}.")

    def display_receipt(self):
        print(Fore.YELLOW + "--------------- Car Sale Receipt "
              "---------------\n" + Fore.RESET)
        if (not self.name or not self.brand or not self.model or not self.date
                or not self.price):
            print("Complete the customer record first.")
            return
        
        print(f"Customer Name\t\t:  {Fore.CYAN + self.name + Fore.RESET}")
        print(f"Car Purchased\t\t:  {Fore.CYAN + self.brand} "
              f"{self.model + Fore.RESET}")
        print(f"Unit Price\t\t:  {Fore.CYAN + self.price} PHP" + Fore.RESET)
        print(f"Date of Purchase\t:  {Fore.CYAN + self.date + Fore.RESET}")
        print(Fore.YELLOW + "\n-------------------------------"
              "-----------------" + Fore.RESET)

    def display_customer_record(self):
        os.system('cls')
        print(Fore.GREEN + "CAR DEALERSHIP" + Fore.RESET)
        print(Fore.YELLOW + "Customer Record\n" + Fore.RESET)
        self.name = input("Enter the customer name: ")
        self.brand = input("Enter the car brand: ")
        self.model = input("Enter the car model: ")
        self.price = input("Enter the unit price: ")
        self.date = input("Enter the date of purchase: ")

    def display_choice(self):
        os.system('cls')
        print(Fore.YELLOW + "Purchase Information\n" + Fore.RESET)
        print("1 - Customer name")
        print("2 - Car's brand and model")
        print("3 - Unit price")
        print("4 - Date of purchase")
        print("5 - Purchase receipt")
        print("\n             0 - Exit\n")

        return input("Enter your choice: ")

    def display_purchase_info(self, choice):
        match choice:
            case '1':
                self.display_name()
                input("\nPress enter to continue.")
            case '2':
                self.display_car()
                input("\nPress enter to continue.")
            case '3':
                self.display_price()
                input("\nPress enter to continue.")
            case '4':
                self.display_date()
                input("\nPress enter to continue.")
            case '5':
                os.system('cls')
                self.display_receipt()
                input("\nPress enter to continue.")
            case '0':
                pass # exit
            case _:
                input("\nInvalid choice. ")

    def menu():
        customer = Customer("", "", "", "", "")
        customer.display_customer_record()
        choice = UNSET_OPTION
        while choice != EXIT_OPTION:
            choice = customer.display_choice()
            customer.display_purchase_info(choice)