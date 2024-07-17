

# --How import work in python --------------------------------------------------------
# importing different modules

# import pandas
# pandas.read_csv()

import math
result= math.sqrt(9)
print(result)
#---------------------------------------------------------------

from math import pi,sqrt 
value=pi* sqrt(36)
print(value)
#--------------------------------------------------------------

# from math import *    imports all functions in math

# "as" keyword 
from math import sqrt as s
a= s(100)
print(a)

import math as m
b= m.isqrt(4)
print(b)
#----------------------------------------------------------------------------

import math
print(dir(math)) # prints all functions

#----------------------------------------------------------------------------

