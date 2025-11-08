def remove_all_file_empty_or_blank_lines(file_path: str):
    """
    This function deletes all empty or blank line of a file.
    """

    with open(file_path, "r+") as f:
        lines = [line for line in f if line.strip()]
        f.seek(0)
        f.writelines(line.rstrip("\n") + "\n" for line in lines)
        f.truncate()
