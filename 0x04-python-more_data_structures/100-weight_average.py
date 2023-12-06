#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    mult, second = 0, 0
    for i in my_list:
        mult += (i[0] * i[1])
        second += i[1]
    return mult / second
