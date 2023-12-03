#!/usr/bin/python3
def no_c(my_string):
    s = ""
    i = 0
    while (i < len(my_string)):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            s += my_string[i]
        i += 1
    return (s)
