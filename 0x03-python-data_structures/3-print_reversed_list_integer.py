#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = -len(my_list)
    m = -1
    while (m >= n):
        print("{}".format(my_list[m]))
        m -= 1
