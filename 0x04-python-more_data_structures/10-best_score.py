#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    max = 0
    for key, value in a_dictionary.items():
        if value > max:
            max = value
    for key, value in a_dictionary.items():
        if value == max:
            return key
