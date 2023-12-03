#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if (my_list == None):
        return
    n = -len(my_list)
    m = -1
    while (m >= n):
        print("{:d}".format(my_list[m]))
        m -= 1
