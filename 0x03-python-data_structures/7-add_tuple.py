#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        a = list(tuple_a)
        a.extend([0] * (2 - len(tuple_a))        
        tuple_a = tuple(a)
    if len(tuple_b) < 2:
        b = list(tuple_b)
        a.extend([0] * (2 - len(tuple_b))
        tuple_b = tuple(b)
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        c = tuple_a[0] + tuple_b[0]
        d = tuple_a[1] + tuple_b[1]
    return (a, b)

