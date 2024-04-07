#!/usr/bin/python3
"""
a program to calc the addetion of two numbers
must be integers

"""
def add_integer(a, b=98):
    """
    Adds two integers or floats after converting them to integers.

    Parameters:
    a (int/float): The first number to add. Must be an integer or float.
    b (int/float, optional): The second number to add. Must be an integer or float. Defaults to 98.

    Returns:
    int: The sum of a and b after converting them to integers.

    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

if __name__=="__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
