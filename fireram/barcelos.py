import os
from colorama import Fore

UNSET_OPTION = -1 
EXIT_OPTION = 0
LARGE_CONTINENT_THRESHOLD = 10_000_000

class Continent ():
    def __init__(self, continent_name, area, population, number_of_countries):
        self.continent_name = continent_name
        self.area = area
        self.population = population
        self.number_of_countries = number_of_countries

    def display_continent_details(self):
        print(Fore.YELLOW 
              + f"==============>{self.continent_name} Details<==============")
        print(Fore.WHITE
              + f"\nName of Continent : {self.continent_name}")
        print(f"Area of the Continent: {self.area} sq km")
        print(f"Population of the Continent: {self.population}")
        print("Number of Countries in the Continent: " 
              + f"{self.number_of_countries}")
        
    def determine_population_density(self):
        density = self.population / self.area
        print(Fore.YELLOW + "Population Density: " 
              + Fore.WHITE + f"{density:.2f} people per sq km")
        return

    def determine_large_continent(self):
        if self.area > LARGE_CONTINENT_THRESHOLD:
            print(Fore.YELLOW + f"{self.continent_name} is a large continent.")
            return
        
        print(f"{self.continent_name} is not a large continent.")
        return
    
    def update_population(self):
        print(Fore.YELLOW + f"Updating population of {self.continent_name}...")
        
        try:
            new_population = int(input(Fore.WHITE 
                                   + "Enter the new population: "))
        except ValueError:
            print(Fore.RED + "Error: Please enter a valid number." 
                  + Fore.RESET )
            return

        self.population = new_population
        print(f"New population updated: {self.population}")

    def add_country(self):
        self.number_of_countries += 1
        print(f"A new country has been added to {self.continent_name}.")
        print(f"\nTotal countries: {self.number_of_countries}")

    def display_menu(self):
        os.system('cls')
        print(Fore.YELLOW + "\n===== Continent Menu =====")
        print(Fore.RESET + "1. Display Continent Details")
        print("2. Calculate Population Density")
        print("3. Check if Large Continent")
        print("4. Update Population")
        print("5. Add a New Country")
        print("0. Exit")
        return int(input(Fore.YELLOW + "Enter your choice: " + Fore.RESET))

    def process_choice(self, choice):
        match choice:
            case 1:
                os.system('cls')
                asia.display_continent_details()
                input(Fore.YELLOW + "Press Enter to continue"+ Fore.RESET)
            case 2:
                os.system('cls')
                asia.determine_population_density()
                input(Fore.YELLOW + "Press Enter to continue"+ Fore.RESET)
            case 3:
                os.system('cls')
                asia.determine_large_continent()
                input(Fore.YELLOW + "Press Enter to continue"+ Fore.RESET)
            case 4:
                os.system('cls')
                asia.update_population()
                input(Fore.YELLOW + "Press Enter to continue"+ Fore.RESET)
            case 5:
                os.system('cls')
                asia.add_country()
                input(Fore.YELLOW + "Press Enter to continue"+ Fore.RESET)
            case 0:
                os.system('cls')
                print("Goodbye")
                input(Fore.YELLOW + "Press Enter to continue"+ Fore.RESET)
            case _:
                print(Fore.YELLOW + "Invalid Choice. Try Again." + Fore.RESET)
                input(Fore.YELLOW + "Press Enter to continue"+ Fore.RESET)

    def start_menu():
        choice = UNSET_OPTION
        while choice != EXIT_OPTION:
            choice = asia.display_menu()
            asia.process_choice(choice)
            os.system('cls')

asia = Continent(continent_name="Asia", area=44_579_000, 
                    population=4_700_000_000, number_of_countries=49)

