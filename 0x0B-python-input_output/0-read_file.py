#!/usr/bin/python3
"""
0x0B. Python - Input/Output
"""


def read_file(filename=""):
    """
    open file
    """
    with open(filename, encoding="utf-8") as f:
        opning = f.read()
        print(opning, end="")
