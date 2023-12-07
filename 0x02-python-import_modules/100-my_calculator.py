#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add,sub,div,mul
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    res = 0
    if (sys.argv[2] == '+'):
        res = add(int(sys.argv[1]),int(sys.argv[3]))
    elif (sys.argv[2] == '-'):
        res = sub(int(sys.argv[1]),int(sys.argv[3]))
    elif (sys.argv[2] == '*'):
        res = mul(int(sys.argv[1]),int(sys.argv[3]))
    elif (sys.argv[2] == '/'):
        res = div(int(sys.argv[1]),int(sys.argv[3]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), res))
