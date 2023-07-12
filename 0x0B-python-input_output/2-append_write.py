#!/usr/bin/python3
"""
0x0B. Python - Input/Output
"""


def append_write(filename="", text=""):
    """
    open file and writes
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
