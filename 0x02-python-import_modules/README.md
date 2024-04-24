pyrhon notes

       - statments in mudule executed only the first time the module name is encountered in an import statemen
       		   (They are also run if the file is executed as a script.)
       - from fibo import * imports all names except those beginning with an underscore (_)
       - options od import :-
       	 import fibo  	   #module then access function as attribute  fibo.fib
	 from fibo import fib, fib2 	#can use function directly (only imported ones)
	 from fibo import *         #import all the funs (not advised)
	 import fibo as fib        #name of module become fib but access function as attribute
	 from fibo import fib as fibonacci      #best one
       - it is advised to use command line arguments with if statement that __name__ == __main__
       - when imported module __name__ is a varaiable contain the module name
       - Python caches compiled version of each module __pycache__ directory under the name module.version.pyc
       - sys.path is a list of strings that determines the interpreter’s search path for modules
       - dir() is used to find out which names a module defines. It returns a sorted list of strings:
       - Without arguments, dir() lists the names you have defined currently
       - Note that it lists all types of names: variables, modules, functions, etc.
       - dir() does not list the names of built-in functions and variables.
       - If you want a list of those, they are defined in the standard module builtins:
       - __init__.py files are required to make Python treat directories containing the file as packages
       - Packages are a way of structuring Python’s module namespace by using “dotted module names”.
       	 For example, the module name A.B designates a submodule named B in a package named A
       - __init__.py code defines a list named __all__, it is taken to be
       	 the list of module names that should be imported when from package import * is encountered.
	 