#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = [0]
    list *= list_length
    divsion = 0
    for i in range(list_length):
        try:
            divsion = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            divsion = 0
        except IndexError:
            print("out of range")
            divsion = 0
        except ZeroDivisionError:
            print("division by 0")
            divsion = 0
        finally:
            list[i] = divsion
    return list