#!/usr/bin/python3
"""
0x0B. Python - Input/Output
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        Student_js = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
        }
        return Student_js
