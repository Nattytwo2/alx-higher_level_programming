#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or not roman_string):
        return 0

    dict_r = {"I": 1,
              "V": 5,
              "X": 10,
              "L": 50,
              "C": 100,
              "D": 500,
              "M": 100}
    num = 0
    lenght = len(roman_string)
    for i in range(lenght):
        if not dict_r.get(roman_string[i], 0):
            return 0
        if (lenght != (i + 1) and
                dict_r[roman_string[i + 1]] > dict_r[roman_string[i]]):
            num += -dict_r[roman_string[i]]
        else:
            num += dict_r[roman_string[i]]
    return num
