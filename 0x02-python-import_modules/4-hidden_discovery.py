#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list = [n for n in dir(hidden_4) if not n.startswith("__")]
    i = 0
    while (i < len(list)):
        print(list[i])
        i += 1
