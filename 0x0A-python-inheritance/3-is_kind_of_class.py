#!/usr/bin/python3
"""
Inheritance
"""


def is_kind_of_class(obj, a_class):
    """Returns true if the object is an instance of or it's
    objects are instance of a class that inherits from the
    specified class"""
    if isinstance(obj, a_class):
        return True
    return False
