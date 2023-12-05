def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return None
    i = my_list[0]
    for ii in my_list:
        if (ii > i):
            i = ii
    return i


my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
