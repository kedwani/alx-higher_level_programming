#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[46-7:73-6] + str[41+73-7:46+73-7] + str[:6]
print(str)
