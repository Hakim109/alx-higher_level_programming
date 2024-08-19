#!/usr/bin/python3

"""
Function to add two integers
prototype: def add_integer(a, b=98):
Returns an integer
"""


def add_integer(a, b=98):
    """
    Addition function.
    Args:
        a (int or float)
        b (int or float, optional)
    Raises:
        TypeError: If either `a` or `b` is not an integer or float.
    Returns:
        int: The result of `a` and `b`
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    # cast numbers into integers if they are float
    a = int(a)
    b = int(b)

    return int(a) + int(b)
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
