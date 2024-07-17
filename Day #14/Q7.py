#--- hard level qustions

'''
STATEMENT-
you will be given 3 integers as a input.
Input may or may not be diff from each other
output should be 1 , if all three integers are different
ore it should be 0 , if repeated more than one time

case1= input  output     |   Case2=   input   output
        3       1        |             100      0
        2                |              5
        1                |              5

'''

a=int(input())
b=int(input())
c=int(input())


if(a!=b and b!=c and c!=a ):
    print(1)
else:
    print(0)   

 