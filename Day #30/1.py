
# RECURSION IN PYTHON- defning something in terms of itself

# Recursive Function - When function calls itelf.........................
'''
for removing factorial in maths we need to write :-
factorial(7)= 7*6*5*4*3*2*1
factorial(6)= 6*5*4*3*2*1
factorial(5)= 5*4*3*2*1
factorial(4)= 4*3*2*1
factorial(3)= 3*2*1
factorial(2)= 2*1
'''
# factorial(n)= n * facorial(n-1)

def factorial(n):
    if(n==1 or n==0):
        return 1             #i.e This can be done without using loops
    else:
        return n * factorial(n - 1)  #function call itself
    
print (factorial(5))
print (factorial(4))
print (factorial(7))

'''
Logic of code=
for factorial n=5
it will take  5*factorial(4)
will take n=4  5*4*factorial(3)
will take n=3 till n=1, and return 1 at last

'''