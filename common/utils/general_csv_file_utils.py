import csv
import os

import csv
import os


def extract_csv(file_path: str) -> list:
    """
    This function extracts data from a csv file: it returns a list of data dictionaries [{}, {}, ...].
    """
    data = []
    with open(file_path, "r") as file:
        csv_reader = csv.DictReader(file)
        for line in csv_reader:
            data.append(line)
    return data


def add_new_line_to_file_csv(file_path: str, line_list: list):
    """
    This function add new line to a csv file and ensure the file ends with a single newline.
    """
    # Add(write) the new line at the end of file:
    with open(file_path, "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(line_list)

    # Ensure the file ends with a single newline:
    with open(file_path, "rb+") as f:
        if f.tell() == 0:
            # File is empty, just write newline
            f.write(b"\n")
            return
        f.seek(-1, os.SEEK_END)
        last_char = f.read(1)
        if last_char != b"\n":
            f.write(b"\n")


if __name__ == "__main__":
    print("\nin film-library-management/write/data/movies.csv\n")

    file_path = "film-library-management/write/data/movies.csv"
    print(f"data = {extract_csv(file_path)}")
    print(f"\ndata type = {type(extract_csv(file_path))}")
    print(f"\ndata length = {len(extract_csv(file_path))}")
    print(f"\ndata the first element = {extract_csv(file_path)[0]}")
    print(f"\ndata type of the first element = {type(extract_csv(file_path)[0])}")
