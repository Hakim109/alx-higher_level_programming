#!/usr/bin/python3
"""class Square"""


class Square:
    """square operation"""
    def __init__(self, size=0):
        """intialize the square
        Args:
            size (int): The size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns square area"""
        return (self.__size ** 2)
