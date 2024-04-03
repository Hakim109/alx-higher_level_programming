#!/usr/bin/python3

"""class MagicClass that does exactly the same as the following Python bytecode"""

import math


class MagicClass:
    """circle."""

    def __init__(self, radius=0):
        """
        Initialize a MagicClass.
        Arguments:
            radius of MagicClass. Must be float or int
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculates and returns the circumference of our MagicClass."""
        return (2 * math.pi * self.__radius)
