#!/usr/bin/python3
""" Class base"""


class Base:
    """Doc string"""
    __nb_objects = 0

    def __init(self, id=None):
        """doc string"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
