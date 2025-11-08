import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from datetime import datetime
from common.models.movie import Movie
from exceptions.movie_exceptions import InvalidTitleException, InvalidYearException, InvalidGenreException, InvalidAgeLimitException


def add_movie():
    """
    This function adds a movie to the list of movies contained in the data file 'file_path'.
    """    
    title, production_year, genre, age_limit = request_movie_data()

    if all(v is not None for v in [title, genre, production_year, age_limit]):
        
        # Create a Movie object:
        movie_object = Movie(title, production_year, genre, age_limit)

        try:
            movie_object.save_to_csv()

        except Exception as e:
            print(f"\nUnexpected error when adding a new line in the csv file {Movie.file_path}: {e}\n")
        
        else:
            print(f"\nThe movie '{movie_object}' was add succesfully.\n")



# --------------------------------- Usuful functions ------------------------------------------
def request_movie_data()->tuple:
    """
    This function allows the user to define information relating to the movie; it checks the validity of this data and generates exceptions if it is not.
    """
    title = production_year = genre = age_limit = None

    try:
        #--title :
        title = input("\n=> Enter the title of the movie to add : ")
        if not title.strip():
            raise InvalidTitleException("\nError: The movie title cannot be empty", title)
        if len(title) > 200:
            raise InvalidTitleException(f"\nError: The movie title cannot contain more than 200 characters. You have entered a title with {len(title)}", title)
        for char in title:
            if not (char.isalpha() or char.isdigit() or char == " "):
                raise InvalidTitleException("\nError: The movie title can only contain letters of the alphabet, numbers, and spaces", title)
                #capitalize the first char only:
        title = title[0].upper() + title[1:]

        #--production_year :
        production_year = input("=> Enter the production year of the movie to add : ")
        if not production_year.isdigit():
            raise InvalidYearException("\nError: The movie's production year can only be a number", production_year)
                #convert production_year to int:
        production_year = int(production_year)
        if not 1895 <= production_year <= int(datetime.now().year):
            raise InvalidYearException(f"\nError: The movie's production year cannot be earlier than 1895 or later than the current year ({datetime.now().year})", production_year)

         #--genre :
        genre = input("=> Enter the genre of the movie to add : ")
        if not genre.strip():
            raise InvalidGenreException("\nError: The movie genre cannot be empty", genre)
        if len(genre) > 50:
            raise InvalidGenreException(f"\nError: The movie genre cannot contain more than 50 characters. You have entered a genre with {len(genre)}", genre)
        for char in genre:
            if not (char.isalpha() or char.isdigit() or char == " "):
                raise InvalidGenreException("\nError: The movie genre can only contain letters of the alphabet, numbers, and spaces", genre)
        
         #--age_limit :
        age_limit = input("=> Enter the age limit for the movie to add (3, 6, 12, 13, 16, 17 or 18) : ")
        if not age_limit.isdigit():
            raise InvalidAgeLimitException("\nError: The age limit for watching the movie can only be a number", age_limit)
                #convert age_limit to int:
        age_limit = int(age_limit)
        if age_limit not in [3, 6, 12, 13, 16, 17, 18]:
            raise InvalidAgeLimitException(f"\nError: The age limit for watching the movie can only be 3, 6, 12, 13, 16, 17 or 18 years old", age_limit)
    except InvalidTitleException as e:
        title = None
        e.display_exception()
    except InvalidYearException as e:
        production_year = None
        e.display_exception()
    except InvalidGenreException as e:
        genre = None
        e.display_exception()
    except InvalidAgeLimitException as e:
        age_limit = None
        e.display_exception()
    
    else:
        print("\nMovie data entry was successful.")

    return title, production_year, genre, age_limit
# ---------------------------------------------------------------------------------------------
    



if __name__=="__main__":
    # file_path = "common/data/movies.csv"

    add_movie()
    # modify_movie(file_path)
    