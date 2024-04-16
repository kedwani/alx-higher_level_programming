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
    # Open the file with specified filename for reading, using UTF-8 encoding
    with open(filename, encoding="utf-8") as f:
        # Read the contents of the file into the variable 'a'
        a = f.read()
        # Print the contents of the file to the console
        print(a, end='')


# If this script is executed directly, for example using 'python read_file.py'
if __name__ == "__main__":
    # Call the read_file function with a default filename (empty string)
    read_file()
