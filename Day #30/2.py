
# Q..Calculation of Fibonacci Series
'''
f0= 0
f1= 1
f2= f1 + f0

f(n) = f(n-1) + f(n-2)......[formula]

'''
# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return(fibonacci(n-1) + fibonacci(n-2))

# nterm= int(input("enter the number:"))

# if nterm <0:
#     print("please enter positive integer")
# else:
#     print("fibonacci sequence:")
#     for i in range (nterm):
#         print(fibonacci(i))



def fibonnaci(n):
    if n<=1:
        return n
    else:
        return(fibonnaci(n-1) + fibonnaci(n-2))

nterm= int(input("enter number:"))
if nterm <0:
    print("enter positive integer!")
else:
    for i in range (nterm):
      print(fibonnaci(i))


