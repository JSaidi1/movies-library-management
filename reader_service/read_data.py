import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from common.models.movie import Movie

def find_movie_by_title():
    """
    This function allows you to find a film in the list of films based on its title.    
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

    

if __name__=="__main__":
    print("in read service")

    find_movie_by_title()