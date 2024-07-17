
# Finally cluase-----------------------------------------------------------
# is used after try: except: and is always executedd

def func1():
    try:
        l=[1,5,6,8]
        i=int(input("enter the index:"))
        print(l[i])
        return 1  # here function is returned, still finally is printed
    except:
        print("Some error occured")
        return 0

    finally:
        print("I am always executed")  # this is always executed

    # print("im important") # this is not executed when this is wraped in a function
                          # and return is used, so finally kyword is used****
x=func1()
print(x)