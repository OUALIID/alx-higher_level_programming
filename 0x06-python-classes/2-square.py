#!/usr/bin/python3
"""Complete a class square."""


class Square:
    """class has a private attribute size and
    the __init__ method validates and initializes
    it with a default of zero."""

    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
