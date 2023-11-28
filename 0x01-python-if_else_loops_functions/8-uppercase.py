#!/usr/bin/python3
def uppercase(str):
    for  o, i in enumerate(str):
        if (ord(i) >= 97 and ord(i) < 123):
            i = chr(ord(i) - 32)
        if (o != len(str) - 1):
           print("{}".format(i), end='')
        else:
            print(i)
