#!/usr/bin/python3
"""
Inheritance
"""


def is_same_class(obj, a_class):
    """Returns true if the object is exactly an instance of the
    specified class, else false"""
    if type(obj) is a_class:
        return True
    return False
