
# Decorators in py ---------------------------------------------------s--------------
# Decorators are tools used to modify the behaviour of functions and methods


def greet(fx):
    def mfx(*args, **kwargs): # for taking arguments of add() function
# *args= take all arguments as tupule, **kwargs= take all arguments as Dict        
        print("Welcome here")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet # this is a decorator which decorates/modofies the hello function
def hello():
    print("This is function hello()")

@greet 
def add(a, b):
    print(f"The number is {a+b}")

hello()
# greet(add)(4, 6)   # if we not use @greet before function
add(4,6)

# ----------------------------------------------------------------------------------

def modi(fx):
    def ufx(*args, **kwargs):
        print("start")
        fx(*args, **kwargs)
        print("End")
    return ufx
@modi
def hello():
    print("this is function")

@modi
def goo(c,d):
    print(c**d) #d times c i.e 4 times 3 i.e 3*3*3*3 = 81

hello()
goo(3,4)

print("--------------------------------------------------------------------------")

def universe(fx):
    def fxr(*args, **kwargs):
        print("good morning")
        fx(*args, **kwargs)
        print("Jai Hind!")
    return fxr

@universe
def world():
    print("Happy Independence Day")

world()
