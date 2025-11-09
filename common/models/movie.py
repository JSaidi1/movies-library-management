import sys
import os
import csv
import tempfile
from typing import List
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from common.utils.csv_file_utils import extract_csv
from common.utils.file_utils import remove_all_file_empty_or_blank_lines
from common.enums.movie_enums import AgeLimit, MovieOperations



class Movie:
    id_cpt = 30  # will be updated from CSV
    file_path = "common/data/movies.csv"
    operation = MovieOperations.DEFAULT # Default operation status

    def __init__(self, id: int, title: str, production_year: int, genre: str, age_limit: int):
        self.id = id
        self.title = title
        self.production_year = production_year
        self.genre = genre
        self.age_limit = age_limit

        if Movie.operation.ADD:
            Movie.id = Movie.load_last_id() + 1

    def __str__(self):
        return f"Movie: identifier: {self.id} - title: {self.title} - production year: {self.production_year} - genre: {self.genre} - age limit: {self.age_limit}"


    @staticmethod
    def load_last_id():
        """
        This static method return the highest ID from the CSV file (0 if file empty).
        """
        try:
            # Remove all file empty or blank lines:
            remove_all_file_empty_or_blank_lines(Movie.file_path)

            # Load:
            if not os.path.exists(Movie.file_path):
                return 0

            with open(Movie.file_path, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                ids = [int(row["id"]) for row in reader]
                return max(ids) if ids else 0

        except Exception as e:
            print(f"\nError when trying to get last id : {e}\n")

    def save_to_csv(
        self, fieldnames=["id", "title", "production_year", "genre", "age_limit"]
    ):
        """
        This method append this movie to the CSV file.
        """
        try:
            # Remove all file empty or blank lines:
            remove_all_file_empty_or_blank_lines(Movie.file_path)

            # Add(write) the new line at the end of file:
            file_exists = os.path.exists(Movie.file_path)

            with open(Movie.file_path, "a", newline="", encoding="utf-8") as csvfile:

                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                if not file_exists:
                    writer.writeheader()

                writer.writerow(
                    {
                        "id": Movie.id,
                        "title": self.title,
                        "production_year": self.production_year,
                        "genre": self.genre,
                        "age_limit": self.age_limit,
                    }
                )

        except Exception as e:
            print(f"\nError when trying to add new movie line in csv file : {e}\n")


    @staticmethod
    def get_movie_by_id(id_movie: int, csv_extracted_data_list: list) -> dict:
        """
        This function return the movie informations if it exists in the list (if not exists it returns an empty dict()). It returns a movie dictionary like {"identifier": "1", "title": "Titanic", ...}
        """

        # Remove all file empty or blank lines:
        remove_all_file_empty_or_blank_lines(Movie.file_path)

        for line in csv_extracted_data_list:
            if id_movie == line["id"]:
                # return Movie(line["title"], line["production_year"], line["genre"], line["age_limit"])
                return line
        return dict()

    @staticmethod
    def show_movies_list(csv_extracted_data_list: list):
        """
        This function displays the list of available films, i.e., those currently saved in the list.
        """

        print("\n=========== Movies List ===========")
        for line in csv_extracted_data_list:
            print(
                f"The movie {line["id"]} => Title : {line["title"]} - Production year : {line["production_year"]} - Genre : {line["genre"]} - Age limit : {line["age_limit"]}"
            )
        print("\n")

    @staticmethod
    def replace_movie(new_movie: dict, id_movie:int):
        """
        This function is used to replace line in csv file by an other new line.
        """

        # Remove all file empty or blank lines:
        remove_all_file_empty_or_blank_lines(Movie.file_path)

        new_line = [f"{new_movie["id"]}", new_movie["title"], new_movie["production_year"], new_movie["genre"], new_movie["age_limit"]]

        # Read all lines
        with open(Movie.file_path, newline="") as f:
            rows = list(csv.reader(f))

        # Replace the line
        rows[id_movie] = new_line

        # Write everything back
        with open(Movie.file_path, "w", newline="") as f:
            csv.writer(f).writerows(rows)
    
    @staticmethod
    def delete_csv_row_by_id(id_movie:str):
        """
        This static method remove a movie from CSV file based on its identifier.
        """
        # Create a secure temporary file in the same directory
        dir_name = os.path.dirname(Movie.file_path)
        with tempfile.NamedTemporaryFile(mode="w", delete=False, newline="", dir=dir_name, encoding="utf-8") as temp_file:
            temp_path = temp_file.name
            
            with open(Movie.file_path, "r", newline="", encoding="utf-8") as f_in:
                reader = csv.DictReader(f_in)
                writer = csv.DictWriter(temp_file, fieldnames=reader.fieldnames)
                writer.writeheader()
                
                for row in reader:
                    if row["id"] != id_movie:
                        writer.writerow(row)
        
        # Replace original file atomically (safe even if program crashes)
        os.replace(temp_path, Movie.file_path)
    
    @staticmethod
    def find_by_title(title_movie: str) -> List[Movie]:
        """
        This function return a list of movies if they exists in the list (if not exists it returns an empty list).
        """
        movies_list = []

        # Remove all file empty or blank lines:
        remove_all_file_empty_or_blank_lines(Movie.file_path)

        # Extract line from csv:
        csv_extracted_data_list = extract_csv(Movie.file_path)

        # find Movie with title:
        for line in csv_extracted_data_list:
            if title_movie.lower() == str(line["title"]).lower():
                movies_list.append(Movie(line["id"], line["title"], line["production_year"], line["genre"], line["age_limit"]))
                
        return movies_list
    
    @staticmethod
    def find_by_age_limit(age_limit: float) -> List[Movie]:
        """
        This function returns a list of movies if their age limit is equals to the age limit given in the input.
        """
        movies_list = []

        # Remove all file empty or blank lines:
        remove_all_file_empty_or_blank_lines(Movie.file_path)

        # Extract line from csv:
        csv_extracted_data_list = extract_csv(Movie.file_path)

        # Find Movies list:
        for line in csv_extracted_data_list:
            if age_limit == float(line["age_limit"]):
                movies_list.append(Movie(line["id"], line["title"], line["production_year"], line["genre"], line["age_limit"]))
                
        return movies_list

    @staticmethod
    def find_by_age_limit_less_than(age_limit: float) -> List[Movie]:
        """
        This function returns a list of movies if their age limit lower than the age limit given in the input.
        """
        movies_list = []

        # Remove all file empty or blank lines:
        remove_all_file_empty_or_blank_lines(Movie.file_path)

        # Extract line from csv:
        csv_extracted_data_list = extract_csv(Movie.file_path)

        # Find Movies list:
        for line in csv_extracted_data_list:
            if age_limit > float(line["age_limit"]):
                movies_list.append(Movie(line["id"], line["title"], line["production_year"], line["genre"], line["age_limit"]))
                
        return movies_list
    
    @staticmethod
    def find_by_age_limit_less_than_or_equals(age_limit: float) -> List[Movie]:
        """
        This function returns a list of movies if their age limit is lower than or equals the age limit given in the input.
        """
        movies_list = []

        # Remove all file empty or blank lines:
        remove_all_file_empty_or_blank_lines(Movie.file_path)

        # Extract line from csv:
        csv_extracted_data_list = extract_csv(Movie.file_path)

        # Find Movies list:
        for line in csv_extracted_data_list:
            if age_limit >= float(line["age_limit"]):
                movies_list.append(Movie(line["id"], line["title"], line["production_year"], line["genre"], line["age_limit"]))
                
        return movies_list
    
    @staticmethod
    def find_by_age_limit_greater_than(age_limit: float) -> List[Movie]:
        """
        This function returns a list of movies if their age limit is greather than the age limit given in the input.
        """
        movies_list = []

        # Remove all file empty or blank lines:
        remove_all_file_empty_or_blank_lines(Movie.file_path)

        # Extract line from csv:
        csv_extracted_data_list = extract_csv(Movie.file_path)

        # Find Movies list:
        for line in csv_extracted_data_list:
            if age_limit < float(line["age_limit"]):
                movies_list.append(Movie(line["id"], line["title"], line["production_year"], line["genre"], line["age_limit"]))
                
        return movies_list
    
    @staticmethod
    def find_by_age_limit_greater_than_or_equals(age_limit: float) -> List[Movie]:
        """
        This function returns a list of movies if their age limit is greather than or equals the age limit given in the input.
        """
        movies_list = []

        # Remove all file empty or blank lines:
        remove_all_file_empty_or_blank_lines(Movie.file_path)

        # Extract line from csv:
        csv_extracted_data_list = extract_csv(Movie.file_path)

        # Find Movies list:
        for line in csv_extracted_data_list:
            if age_limit <= float(line["age_limit"]):
                movies_list.append(Movie(line["id"], line["title"], line["production_year"], line["genre"], line["age_limit"]))
                
        return movies_list
    

if __name__ == "__main__":
    print("in /write/movie.py")

    file_path = "common/data/movies.csv"

    # Extract movies data from the csv file:
    csv_extracted_data_list = extract_csv(Movie.file_path)

    # movie_1 = Movie("Title1", 1970, "Drama", 18)
    # print(Movie.movie_object_operation_is(MovieOperations.ADD.name))

    # list_movies = Movie.find_by_title("The Silence of the Lambs")
    # list_movies = Movie.find_by_age_limit(15)
    # list_movies = Movie.find_by_age_limit_lower_than_or_equals(6)
    # list_movies = Movie.find_by_age_limit_greater_than(17)
    list_movies = Movie.find_by_age_limit_greater_than_or_equals(6)
    for movie in list_movies:
        print("Movies : ", movie)

    
    
