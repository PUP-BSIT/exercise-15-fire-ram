import os

CURRENT_YEAR = 2024
EXIT_OPTION = 0
UNSET_OPTION = -1
CLASSIC_MOVIE = 20
GOOD_RATING_MOVIE = 8
MID_RATING_MOVIE = 5

class Movie: 
    def __init__(self, title, director, rating, year, genre):
        self.title = title
        self.director = director
        self.rating = rating
        self.year = year
        self.genre = genre

    def get_movie_title(self):
        print(f"The movie title is '{self.title}'" 
                f" and it's directed by {self.director}.")

    def get_rate(self):
        print(f"The movie '{self.title}' now has a rating" 
                f" of {self.rating}/10.")

    def determine_classic(self):
        if CURRENT_YEAR - self.year > CLASSIC_MOVIE:
            print(f"The movie '{self.title}' is classic .")
            return
        
        print(f"The movie '{self.title}' not yet a classic.")

    def recommend(self):
        if self.rating >= GOOD_RATING_MOVIE:
            print(f"The movie '{self.title}' is highly recommended. ")
        elif MID_RATING_MOVIE <= self.rating < GOOD_RATING_MOVIE:
            print(f"The movie '{self.title}' is worth watching. ")
        else:
            print(f"The movie '{self.title}' might not like by everyone.")

    def display_movie_information(self):
        print(f"Movie title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Rating: {self.rating}/10")
        print(f"Year: {self.year}")
        print(f"Genre: {self.genre}")
    
    def user_input(self):
        self.title = input("Enter the movie title: ")
        self.director = input("Enter the director: ")
        self.rating = int(input("Enter the rating (1/10): "))
        self.year = int(input("Enter the year: "))
        self.genre = input("Enter the genre: ")

    def menu():
        os.system("cls")  
        movie1 = Movie("", "", "", "", "")
        movie1.user_input()
        choice = UNSET_OPTION
        while choice != EXIT_OPTION:
            choice = movie1.display_choice()
            movie1.process_choice(choice)
            os.system("cls")

    def display_choice(self):
        os.system("cls")
        print("Movie Choice")
        print("1. Movie")
        print("2. Ratings")
        print("3. Classic or Not Classic")
        print("4. Recommend")
        print("5. Display Movie information")
        print("0. Exit")

        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return -1 
  
    def process_choice(self, choice):
        os.system("cls")
        match choice:
            case 1:
                self.get_movie_title()
                input("\nPress Enter to continue.")   
            case 2:
                self.get_rate()
                input("\nPress Enter to continue.")   
            case 3:
                self.determine_classic()
                input("\nPress Enter to continue.")   
            case 4:
                self.recommend()
                input("\nPress Enter to continue.")   
            case 5:
                self.display_movie_information()
                input("\nPress Enter to continue.")   
            case 0:
                pass
            case _:
                print("Invalid choice")
                input("\nPress Enter to continue.")   