#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx >= len(my_list) or idx < 0):
        ls = my_list[:]
        return ls
    ls = my_list[:]
    ls[idx] = element
    return (ls)
