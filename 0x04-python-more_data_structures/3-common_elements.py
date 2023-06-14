#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_listing = []
    for i in set_1:
        for j in set_2:
            if i == j:
                new_listing.append(i)
    return new_listing
