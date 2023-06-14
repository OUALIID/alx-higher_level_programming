#!/usr/bin/python3
def multiply_by_2(dictionary_p):
    dictionary_o = dictionary_p.copy()
    for key in dictionary_o:
        dictionary_o[key] = dictionary_o[key] * 2
    return dictionary_o
