#!/usr/bin/python3
import random
number = 0
str_num = str(number)
if number < 0:
    num = int(str_num[-1]) * -1
elif number > 0:
    num = int(str_num[-1])
if num == 0:
    str_num1 = "and is zero"
elif num < 6:
    str_num1 = "and is less than 6 and not 0"
elif num > 5:
    str_num1 = "and is greater than 5"
print("Last digit of", number, "is", num,  str_num1)
