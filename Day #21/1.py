
# ---  FUNCTION  ARGUMENTS & RETURN  Statements
'''
four types of arguments:-
Default Argument
Required Argument
keyword Argument
Variable length Argument
'''

def average(a,b):
    print("The average is", (a+b)/2)   #this is  FUNCT

average(2,3)


print("-------------------------------------------------------------------")
#-- for Default Argument
print('This is Default argument')
def average(a=5,b=10, c=1):    #values are specified
    print("The average is", (a+b+c)/2)  

average(2,3)  # we can give default value for the function, which will be printed
# average(a=2)
# average(b=8)


print("--------------------------------------------------------------------")
#-- for keyword argument
print("This is keyword argument")
def average(a=5,b=10, c=1):    #values are specified
    print("The average is", (a+b+c)/2)  

# average(2,3)   this is in serial manner i.e a=2, b=3
# we can give instead key value pair, without serial manner
average(b=3, a=24, c=2)


print("--------------------------------------------------------------------")
#-- for Required Argument
print("This is required argument")
def average(a,b=15):    # if a value is not defined
    print("The average is", (a+b)/2)   

average(a=4)  # this is required argument, we have to define value for a (any)


print("--------------------------------------------------------------------")
#-- for variable length argument
print("this is variable length argument")

def average(*numbers):       # this is tupule****************
    sum=0
    for i in numbers:
        sum = sum+i
    print("Average is:", sum/len(numbers))

average(12,3,6,5,56,8)



def name(**name):           # this is dict***************
    print("hello", name["fname"], name["mname"], name["lname"],'.')

name(mname="shankar", fname="pratik", lname="Amundkar")



print("----------------------------------------------------------------------------------")
print("This is RETURN statement")

def average(*numbers):       
    sum=0
    for i in numbers:
        sum = sum+i
    return sum / len(numbers)
  # return 6

c= average(12,3,6,5,56,8)
print(c)