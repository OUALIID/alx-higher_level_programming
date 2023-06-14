#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_cop = my_list.copy()
    for i in range(len(list_cop)):
        if list_cop[i] == search:
            list_cop[i] = replace
    return list_cop