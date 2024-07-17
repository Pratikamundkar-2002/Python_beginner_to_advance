

# Local & Global Variables---------------------------------------------------

x=10  # global variable(can be print globally)


def my_function():
    global x  # we can change global x value from within the function by [global keyword]
    x=4

    y=5    #Local variable (as defined in a function )
    print(y)

my_function()
# print(y)   #we cannot run local Var outside the function in which it is wraped.
print(x) # here global x in function will be printed
