#!/usr/bin/python3
"""
0x0B. Python - Input/Output
"""


def write_file(filename="", text=""):
    """
    open file and writes
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
