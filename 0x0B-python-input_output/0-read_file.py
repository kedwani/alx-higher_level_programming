#!/usr/bin/python3

def read_file(filename=""):
    """
    Read the contents of a file and print them to the console.

    Parameters:
    filename (str): name of file to read. If not provided empty string is used,
                    which will read from a file with an empty filename.

    Raises:
    FileNotFoundError: If file cannot be found or opened for reading.

    Returns:
    None
    """
    with open(filename, encoding="utf-8") as f:
        a = f.read()
        print(a, end='')


    if __name__ == "__main__":
    read_file()
