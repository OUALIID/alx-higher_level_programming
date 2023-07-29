#!/usr/bin/python3
"""
0x0B. Python - Input/Output
"""


def class_to_json(obj):
    """
    This line defines the function `class_to_json`,
    which takes one parameter `obj`,
    representing an instance of a class.
    The `vars()` function takes an object as its argument
    and returns a dictionary representation of that object's attributes.
    In this context `obj` is an instance of a class, and `vars(obj)`
    retrieves a dictionary containing all the attributes of that instance.
    """
    return vars(obj)
