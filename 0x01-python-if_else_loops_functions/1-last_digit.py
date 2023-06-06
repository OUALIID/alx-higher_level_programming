#!/usr/bin/python3
import random
number  = random.randint(-10000, 10000)
str_num = str(number)
if number < 0:
    num_p = int(str_num[-1]) * -1
elif number > 0:
    num_p = int(str_num[-1])
if num_p == 0:
    str_num1 = "and is zero"
elif num_p < 6:
    str_num1 = "and is less than 6 and not 0"
elif num_p > 5:
    str_num1 = "and is greater than 5"
print("Last digit of", number, "is", num_p,  str_num1)
