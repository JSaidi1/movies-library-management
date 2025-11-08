import csv


def extract_csv(file_path) -> list:
    """
    This function extracts data from a csv file: it returns a list of data dictionaries [{}, {}, ...].
    """
    data = []
    with open(file_path, "r") as file:
        csv_reader = csv.DictReader(file)
        for line in csv_reader:
            data.append(line)
    return data

if __name__ == "__main__":
    print("\nin film-library-management/write/data/movies.csv\n")

    file_path = "film-library-management/write/data/movies.csv"
    print(f"data = {extract_csv(file_path)}")
    print(f"\ndata type = {type(extract_csv(file_path))}")
    print(f"\ndata length = {len(extract_csv(file_path))}")
    print(f"\ndata the first element = {extract_csv(file_path)[0]}")
    print(f"\ndata type of the first element = {type(extract_csv(file_path)[0])}")