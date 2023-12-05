#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    l = my_list.copy()
    for i in range(0, len(l)):
        if (my_list[i] % 2 == 0):
            l[i] = True
        else:
            l[i] = False
    return l
