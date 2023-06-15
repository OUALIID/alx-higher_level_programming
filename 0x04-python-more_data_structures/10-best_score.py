#!/usr/bin/python3
def best_score(dictionary_a):
    if dictionary_a is None:
        return None
    max_value = float('-inf')
    max_key = None
    for key, val in dictionary_a.items():
        if val > max_value:
            max_value = val
            max_key = key
    return max_key

