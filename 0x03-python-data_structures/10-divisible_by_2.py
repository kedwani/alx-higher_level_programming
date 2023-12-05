#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    ll = my_list.copy()
    for i in range(0, len(ll)):
        if (my_list[i] % 2 == 0):
            ll[i] = True
        else:
            ll[i] = False
    return ll
