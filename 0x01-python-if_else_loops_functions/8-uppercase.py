#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if (ord(i) >= 97 and ord(i) < 123):
            print("{}".format(chr(ord(i) + 55)), end='')
        else:
            print(i, end='')
