
# LAMBDA FUNCTIONS (carry out arithematic operations)

# def double(x):
#     return x*2
# print(double(5))  # it will print 5*2=10

# instead of this we can write this as--------------

double= lambda x: x*2
cube= lambda x: x*x*x
avg= lambda x, y, z: (x + y + z)/ 3

print(double(8))
print(cube(5))
print(avg(3,5,10))
