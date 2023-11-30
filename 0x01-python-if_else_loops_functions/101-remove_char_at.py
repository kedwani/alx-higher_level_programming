#!/usr/bin/python3
def remove_char_at(str, n):
    a = ""
    c = 0
    for i in str:
        if (c != n):
            a += i
        c += 1
    return (a)
