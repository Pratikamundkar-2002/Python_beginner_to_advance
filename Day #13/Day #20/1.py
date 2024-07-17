#     FUNCTIONS IN PYTHON _______________
'''
we call function in python for specific condition
functions are called ,
asume you are using a block of code 10 to 50 times in your program which is (15-20 lines)
we can specify a function to it, or wrap it in a function
and call it whenever needed in a big program..
this reduces the code and work 

There are two types :-
Built-in Functions
min(), max(), len(), sum(), type(), range(), dict(), list(), tupule(), print(),etc
User-defined Functions
'''

# if we want to remove a geometric mean of again and again we need to write the 
# formula again and again

a=9
b=8
gmean1= (a*b)/(a+b) #we need to write this again and again, it can be sometimes of 50 lines
print(gmean1)


c=10
d=4
gmean2= (c*d)/(c+d)
print(gmean2)

print("--------------------------------------------------------------------")
# so we write a fuction and call it each time

def calculateGmean(a, b):  #}      #def is used to Define a function
    mean = (a*b)/(a+b)     #}this is user defined  function 
    print(mean)            #}

def isgreater(a,b):
    if (a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")    

def islesser(a,b):
    pass                 #is used when we want to write function afterwards
              
a=9
b=8
calculateGmean(a,b)
isgreater(a,b)

'''if (a>b):
        print("First number is greater")
else:
        print("Second number is greater or equal") 
    
---------IF WE WANT TO APPLY THIS CONDITION FOR EVERY MEAN CALCULATION ,
 We Need to type this Everytime, so we write above function '''
              
c=10
d=4
calculateGmean(c,d)
isgreater(c,d)

e=100
f=200
calculateGmean(e,f)
isgreater(e,f)