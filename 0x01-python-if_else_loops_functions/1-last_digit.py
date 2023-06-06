#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_num = str(number)
if number < 0:
    last = int(str_num[-1]) * -1
elif number > 0:
    last = int(str_num[-1])
if last == 0:
    str_tmp = "and is zero"
elif last < 6:
    str_tmp = "and is less than 6 and not 0"
elif last > 5:
    str_tmp = "and is greater than 5"

print("Last digit of", number, "is", last, "and", str_tmp)
