#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    i = 1
    sum = 0
    while (i < argc):
        sum += int(sys.argv[i])
        i += 1
    print("{}".format(sum))
