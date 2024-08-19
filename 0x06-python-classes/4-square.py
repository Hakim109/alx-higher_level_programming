#!/usr/bin/python3
"""class Square"""


class Square:
    """square operation"""
    def __init__(self, size=0):
        """intialize
        Args:
            size (int): square size
        """
        self.size = size

    def area(self):
        """returns square area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size
        Args:
            value (int): size value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
