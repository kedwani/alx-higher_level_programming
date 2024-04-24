not empty
on task 10 i have solved it by searching backward instide the list and i got a
effecincy error so i tried again by searching forward and it worked
can found the old code in a file with the same name but appended by "old_code"


on python :
   - division always returns a floating point number
   - to get an integer result you can use the // operator(same as / but return integer)
   - In interactive mode, the last printed expression is assigned to the variable _
   - to use print without interpret special characters like "\n" simply add an r before "str" ike follw
   print(r"i need not to interpret new line chracter\n\n\n")
   - to print multiple lines. we should triple-quotes: """...""" or '''...'''.
   - Strings concatenated with the + operator, and repeated with *
   - Two or more string literals next to each other are automatically concatenated like
   'Py' 'thon'  >>>>   'Python'
   - Strings can be indexed - consider itis a list of characters starts with zero and Indices may also be
   negative numbers, to start counting from the right (starts with -1)
   - slicing is supported, Slice indices have useful defaults fisrt is zero , second is the last char
   the first is encluded while the seconed is excluded.
   - Python strings cannot be changed so ssigning to an indexed position not supported
   - str.format() Method >> to pass variables to str as follows
   name = "kedwani"
   age = 15
   "Hello, {}! You're {} years old.".format(name, age)
   -f"" also used to format string with specifiers like that
   age = 24
   print(f"i am {age:d} years old")
   #:d used to format output to be integer
   #:f used to format output to be float