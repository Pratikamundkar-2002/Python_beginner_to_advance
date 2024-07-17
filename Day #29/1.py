# ................Docstrings in python.........................
#  docstrings are string literal that appear right after def of function ,class, method or module
 
def square(n):
    '''Takes in a number n, returns the square of n''' #this is DOCSTRING & not comment
    print(n**2)
square(5)
square(3)
square(6)
print(square.__doc__)   #we can print doc string like this.......

# PEP 8
# Zen in python



