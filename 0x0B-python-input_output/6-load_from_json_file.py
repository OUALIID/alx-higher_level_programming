#!/usr/bin/python3
"""
0x0B. Python - Input/Output
"""
import json


def load_from_json_file(filename):
    """
    open file and writes
    """
    with open(filename, "r", encoding='utf-8') as f:
        load = f.read()
        return json.loads(load)
