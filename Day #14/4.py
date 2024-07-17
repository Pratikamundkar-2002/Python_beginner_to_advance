#----Nested-if statements --------------------------------

num=51
if(num<0):
    print("the number is negative")
elif(num>0):
    if(num>1 and num<=20):
        print("the mumber is between 2 to 20")
    elif(num>20 and num<=50):
        print("the number is between 21 to 50")
    else:
        print("the number is greater than 50")
else:
    print("the umber is equal to 0")            
   