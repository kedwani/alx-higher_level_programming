python notes
       - A for or while loop canused with else,  In a for loop, else is executed after the loop reaches its final iteration. and In a while loop, it’s executed after the loop’s condition becomes false.
       - else is not executed if the loop was terminated by a break.
       - match statment act as witch as follows
       match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
	-“variable name” _ acts as defualt .
	- You can combine several condetions in a single pattern using | (“or”) as follow
	case 401 | 403 | 404:
    	     return "Not allowed"
	- every function even those without a return actually return None
	- the specifier are used like this {field_name:conversion}
	s for string,
	d to display decimal integers (10-base),
	f for float
	- we cannot use d with float but we can use .0f to display it as integer
	- the padding used the same as specifier {field_name:padding},
	- by default strings are left-justified within the field, and numbers are right-justified
	- to modify this:-
	  < will left-align the text in a field.
	  ^ will center the text in the field.
	  > will right-align it
	- field filled  with whitespace characters , to modefy this we write the
	  desired char before the padding like this {:*^20s}
	- 