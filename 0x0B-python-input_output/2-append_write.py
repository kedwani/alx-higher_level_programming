#!/usr/bin/python3
"""
file contain append_write function
"""


def append_write(filename="", text=""):
    """
    a function to append text to a file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
