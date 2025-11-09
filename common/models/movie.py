import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import csv
import os

from common.utils.file_utils import remove_all_file_empty_or_blank_lines


class Movie:
    id = 30  # will be updated from CSV
    file_path = "common/data/movies.csv"

    def __init__(self, title: str, production_year: int, genre: str, age_limit: int):
        self.title = title
        self.production_year = production_year
        self.genre = genre
        self.age_limit = age_limit

        Movie.id = Movie.load_last_id() + 1

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
    

    def __str__(self):
        return f"Movie: identifier: {Movie.id} - title: {self.title} - production year: {self.production_year} - genre: {self.genre} - age limit: {self.age_limit}"


if __name__ == "__main__":
    print("in /write/movie.py")

    movie_1 = Movie("Title1", 1970, "Drama", 18)
