
# Raising Custom ERRORS--------------------------------------------------------------

a= int(input("print numbers between 5 and 9:"))
   #we want that user should give input beyween 5&9 only

if (a<5 or a>9):
    raise ValueError("value should between 5 & 9")
    # we can raise any custom errors for the program we want 
    # so user should understand that what we want him to input
# (google:built-in-exceptions) for types of error we can raise

