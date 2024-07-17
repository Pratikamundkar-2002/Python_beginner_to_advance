#  TYPECASTING IN PYTHON----------- conversion of one datatype into other------

a='1'
b='2'
# this is not integer it is string so it will print 1+2 = 12
print(a+b)

# so we can convert this string to integer--------------
print(int(a) + int(b))
# ^ here it will print the string in integer form i.e number



# There are two types
# IMPLICIT AND EXPLICIT casting----------------------------

# Implicit the conversion is done by python interpreter.
c=12
d=1.5
print(c+ d)  # c is automatically converted to float

# Explicit is conversion done by us according to need.
e='10'
d= 2
print(int(e) + d)   # e is string and converted into number