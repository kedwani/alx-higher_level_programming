#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set(map((lambda x: x), my_list))
    sum = 0
    for i in a:
        sum += int(i)
    return (sum)
