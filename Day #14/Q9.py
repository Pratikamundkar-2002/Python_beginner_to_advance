'''
STATEMENT-
pythogorean triplet is= [a*a + b*b = c*c]
you will be given three numbers 
you have to output 1 if they form a pythagorean triplet
or you havr to output 0
'''

a=int(input())
b=int(input())
c=int(input())

if(a*a+b*b==c*c) or (a*a+c*c==b*b) or (b*b+c*c==a*a):
    print(1)
else:
    print(0)    