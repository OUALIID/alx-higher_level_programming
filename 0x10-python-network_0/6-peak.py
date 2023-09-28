#!/usr/bin/python3
# A function that finds a vertex in a list of unsorted integers.


def find_peak(list_of_integers):
    """the function find_peak"""
    for i in range(1, len(list_of_integers) - 1):
        prev = list_of_integers[i - 1]
        follow = list_of_integers[i + 1]
        curren = list_of_integers[i]
        if curren > prev and curren > follow:
            return curren
    list_of = list_of_integers 
    if (len(list_of) >= 2 and list_of[0] >= list_of[1]):
        return list_of_integers[0]
    if (len(list_of) >= 2 and list_of[-2] <= list_of[-1]):
        return list_of[-1]
    return  None
