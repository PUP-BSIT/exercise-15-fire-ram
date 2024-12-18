import os

EXIT_OPTION = "7"
UNSET_OPTION = ""

class MySelf:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def show_name(self):
        return f"\nHello, my name is {self.name}."
    
    def show_age(self):
        return f"\nI am {self.age} years old."
    
    def show_location(self):
        return f"\nI live in {self.location}."

    def update_name(self, new_name):
        self.name = new_name
        return f"Your name has been updated to {self.name}."
    
    def update_age(self, new_age):
        try:
            self.age = int(new_age)
            return f"Your age has been updated to {self.age}."
        except ValueError:
            return "Invalid input. Please enter a valid integer for age."
    
    def update_location(self, new_location):
        self.location = new_location
        return f"Your location has been updated to {self.location}."

    def menu():
        os.system("cls")
        choice = UNSET_OPTION
        while choice != EXIT_OPTION:
            choice = person_1.display_get_choice()
            person_1.process_choice(choice)
            os.system("cls")
    
    def display_get_choice(self):
        print("\n")
        print("<++++++++++> Menu <++++++++++>")
        print("=                            =")
        print("=    1. Show Name            =")
        print("=    2. Show Age             =")
        print("=    3. Show Location        =")
        print("=    4. Update Name          =")
        print("=    5. Update Age           =")
        print("=    6. Update Location      =")
        print("=    7. Back To Main Menu    =")
        print("=                            =")
        print("<++++++++++++++++++++++++++++>")

        return input("\nSelect an option: ")
    
    def process_choice(self, choice):
        match choice:
            case '1':
                print(self.show_name())
                input("\nPlease press enter key to continue...")
            case '2':
                print(self.show_age())
                input("\nPlease press enter key to continue...")
            case '3':
                print(self.show_location())
                input("\nPlease press enter key to continue...")
            case '4':
                new_name = input("\nEnter new name: ")
                print(self.update_name(new_name))
                input("\nPlease press enter key to continue...")
            case '5':
                new_age = input("\nEnter new age: ")
                print(self.update_age(new_age))
                input("\nPlease press enter key to continue...")
            case '6':
                new_location = input("\nEnter new location: ")
                print(self.update_location(new_location))
                input("\nPlease press enter key to continue...")
            case '7':
                print("\nExiting the menu...")
                input("\nPlease press enter key!")
            case _:
                print("\nInvalid option. Please try again.")  
                input("\nPlease press enter key to continue...")

person_1 = MySelf(name="Gener", age=20, location="Parañaque City, Philippines")