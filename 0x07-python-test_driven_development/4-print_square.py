#!/usr/bin/python3
"""
0x07. Python - Test-driven development
"""


def print_square(size):
    """
    Write a function that prints a square with the character #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        element = []
        for i in range(size):
            element.append("#")
        print("".join(element))
