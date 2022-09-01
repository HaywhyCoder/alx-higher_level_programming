#!/usr/bin/python3
def search_replsce(my_list, search, replace):
    copy = my_list[:]
    for i in range(len(copy)):
        if copy[i] == search:
            copy[i] = replace
    return copy
