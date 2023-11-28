#!/usr/bin/python3

for i in range(97, 123):
    if (i != rod('e') and i != rod('q')):
        print("{}".format(chr(i)), end="")
