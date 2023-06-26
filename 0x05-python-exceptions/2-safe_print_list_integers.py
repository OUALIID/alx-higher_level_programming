#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    M = []
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                M.append(my_list[i])
        except (ValueError, TypeError):
            continue
    for i in M:
        print("{:d}".format(i), end="")
        count += 1
    print()
    return count
