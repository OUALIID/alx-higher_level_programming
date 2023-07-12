#!/usr/bin/python3
"""
0x0B. Python - Input/Output
"""


def read_file(filename=""):
    """
    open file
    """
    with open("my_file_0.txt", encoding="utf-8") as f:
        opning = f.read()
        for i in opning:
            print(i, end="")
