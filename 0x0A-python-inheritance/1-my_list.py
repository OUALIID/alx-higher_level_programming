#!/usr/bin/python3
"""
Inheritance from the class list
"""


class MyList(list):
    """The class MyList that inherits from list"""

    def print_sorted(self):
        """Public instance method"""
        sorted_list = sorted(self)
        print(sorted_list)
