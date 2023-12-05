def divisible_by_2(my_list=[]):
    s = my_list.copy()
    for i in range(0,len(s)):
        if ((my_list[i] % 2) == 0):
            s[i] = True
        else:
            s[i] = False
    print(len(s))
    return (s)



my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
