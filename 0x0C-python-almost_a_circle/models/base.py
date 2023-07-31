#!/usr/bin/python3
<<<<<<< HEAD
""" Class base"""


class Base:
    """Doc string"""
    __nb_objects = 0

    def __init(self, id=None):
        """doc string"""
=======
"""
0x0C. Python - Almost a circle
"""


class Base:
    """
    first class Base.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor.
        """
>>>>>>> 8e1cef4920aba1f9dae6a13e9bb49f874be46496
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
<<<<<<< HEAD
            self.id = self.__nb_objects
=======
            self.id = Base.__nb_objects
>>>>>>> 8e1cef4920aba1f9dae6a13e9bb49f874be46496
