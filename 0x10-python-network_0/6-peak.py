#!/usr/bin/python3
# A function that finds a vertex in a list of unsorted integers.


def find_peak(list_of_integers):
    """A function that returns the peak"""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    return None
