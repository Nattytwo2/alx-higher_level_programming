#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        k = list(a_dictionary.keys())[list(a_dictionary.values()).index(value)]
        if a_dictionary[k]:
            del a_dictionary[k]
    return a_dictionary
