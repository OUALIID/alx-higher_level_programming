#!/usr/bin/python3
"""
0x0B. Python - Input/Output
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            for attr in attrs:
                if not isinstance(attr, str):
                    pass

                else:
                    dictionary = {}
                    for attr in attrs:
                        if hasattr(self, attr):
                            dictionary[attr] = getattr(self, attr)
                    return dictionary
        else:
            dictionary = {
                'age': self.age,
                'last_name': self.last_name,
                'first_name': self.first_name
            }
            return dictionary
