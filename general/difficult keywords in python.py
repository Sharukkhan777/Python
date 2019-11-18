# list of some keywords and its uses
#------------------------------------------------------------------------------
# is keyword
# check whether the memory address are same 

a = b = [1,2,3]
c = [1,2,3]
a is b  # True
a is c  # False
#------------------------------------------------------------------------------
# as keyword 
# use for make alias names 
# object will save in same memory address if we use as keyword

import numpy
import numpy as np
id(numpy) == id(np)
# for example

list = [1,2,3]
id(list[0]) #140709017588544 'This number Represents memory address'
id(list[1]) #140709017588576 increased by 16
id(list[2]) #140709017588608 increased by 16
#id() (or its equivalent) is used in the is operator.
#------------------------------------------------------------------------------
# global keyword

# global keyword is use to make the variable access anywhere in the program
# even if it is inside the function

#create a function:
def myfunction():
  global x
  x = "hello"

#execute the function:
myfunction()

#x should now be global, and accessible in the global scope.
print(x)










































































































