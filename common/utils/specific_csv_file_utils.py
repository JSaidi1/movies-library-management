def show_movies_list(file_path: str, csv_extracted_data_list: list):
    """
    This function displays the list of available films, i.e., those currently saved in the list.
    """
    print("\n=========== Movies List ===========")
    for line in csv_extracted_data_list:
        print(
            f"The movie {line["id"]} => Titre : {line["titre"]} - Année de production : {line["annee_production"]} - Genre : {line["genre"]} - Age limite : {line["age_limite"]}"
        )
    print("\n")

def get_movie_by_id(id_movie: int, csv_extracted_data_list: list) -> dict:
    """
    This function return the movie informations if it exists in the list (if not exists it returns an empty dict()). It returns a movie dictionary like {"identifier": "1", "title": "Titanic", ...}
    """
    for line in csv_extracted_data_list:
        if id_movie == line["id"]:
            return line
    return dict()
