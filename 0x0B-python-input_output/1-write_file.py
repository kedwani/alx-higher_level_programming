#!/usr/bin/python3
"""
a file contain write_file function
"""


def write_file(filename="", text=""):
    """
    rite text to a file.

    This function writes the provided text to a file specified by the filename.

    Parameters:
    filename (str): name of the file to write to. Defaults to an empty string.
    text (str): text to be written to the file. Defaults to an empty string.

    Returns:
    int: The number of characters written to the file.


    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
