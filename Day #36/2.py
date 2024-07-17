# we can write multiple except for try

try:
    num= int(input("Enter an integer:"))
    a= [6,3]  #index
    print(a[num])
except ValueError:    #if value error occurs , print("")
    print("number is not correct")
except IndexError:
    print("index error") #will occur when input number out of index
