import sys
from pathlib import Path
from typing import List

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from common.models.movie import Movie
from common.utils.string_utils import is_numeric

def find_movie_by_title():
    """
    This function allows you to find a movie in the list of films based on its title.    
    """
    # Request the title of movie to find:
    title_movie_to_find = input("Enter the title of the movie you are looking for : ")

    # Check input title:
    if len(title_movie_to_find) <= 200:

        if Movie.find_by_title(title_movie_to_find):

            print(f"\nMovie(s) with title '{title_movie_to_find}' are : ")

            for movie in Movie.find_by_title(title_movie_to_find):
                
                print(movie)
            print("\n")
        else:
            print(f"\nNo movie found whith the title '{title_movie_to_find}'\n")

    else:
        print(f"\nError: title movie length cannot exceed 200 characters. You have entered {len(title_movie_to_find)} charecter.\n")


def find_movies_with_age_limit_less_than_or_equal():
    """
    This function allows you to find a list of movies in the list which age limite is less or equals a value given in the input.
    """
    
    # Request the age limit of movies to find:
    age_limit = input("Enter the age limit to find movie(s) with age limit less or equals this value : ")

    if is_numeric(age_limit):
        
        for movie in Movie.find_by_age_limit_less_than_or_equals(float(age_limit)):
            print(movie)
        print("\n")

    else:
        print(f"\nInvalid age limit (It must be a positive number) not {age_limit}")

def find_movies_by_genre():
    """
    This function returns a list of movies with a specific genre.
    """
    
    # Request the genre of movies to find:
    genre = input("Enter the genre of movie(s) to find : ")

    if len(genre) <= 50:
        
        for movie in Movie.find_by_genre(genre):
            print(movie)
        print("\n")

    else:
        print(f"\nError: genre movie length cannot exceed 50 characters. You have entered {len(genre)} charecter.\n")

def find_movies_by_production_year_between_start_and_end_year():
    """
    This function allows you to find a list of movies in the list which production year is between a start and end year.
    """
    # Request the start and end year:
    start_year = input("Enter the start year : ")
    end_year = input("Enter the end year : ")

    if start_year.isdigit() and end_year.isdigit():

        if int(start_year) < int(end_year):

            for movie in Movie.find_by_production_year_between_start_and_end_year(int(start_year), int(end_year)):
                print(movie)
            print("\n")
        
        else:
            print(f"\nstart year must be less than end year. You entered start_year = {start_year} and end_year = {end_year}")

    else:
        print(f"\nInvalid start or end year. You entered start_year = {start_year} and end_year = {end_year}")



if __name__=="__main__":
    print("in read service")

    # find_movie_by_title()
    # find_movies_with_age_limit_less_than_or_equal()
    # find_movies_by_genre()
    find_movies_by_production_year_between_start_and_end_year()
