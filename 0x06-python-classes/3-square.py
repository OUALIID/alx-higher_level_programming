#!/usr/bin/python3
"""Completing the class Square"""


class Square:
    """The Square class has a private attribute size and
    the __init__ method handles size
    validation and initialization."""

    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2
