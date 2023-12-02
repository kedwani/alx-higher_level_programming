#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from add_0 import add
    a = sys.argv[1]
    b = sys.argv[2]
    number = add(a, b)
    print("{} + {} = {}".format(a, b, number)
