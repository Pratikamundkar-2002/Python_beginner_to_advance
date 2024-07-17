
# Exception Handling In PYTHON-(error handling)------------------------------------

'''
a= input("Enter the number:")
print(f"multiplication table of {a} is:")

for i in range(1 ,12):
    print(f"{int(a)} X {i} = {int(a)*i} ")
# If someone type input as "Harry" then Error will occur
# and if there are some imp lines after that, will not be printed
# as python stops the execution after the error ie. program takes halt 
print("some imp lines of code")
print("End of program")
#SO WE USE try-except Exception to handle error and print further program
'''

a= input("Enter the number:")
print(f"multiplication table of {a} is:")

try:
    for i in range(1 ,12):
        print(f"{int(a)} X {i} = {int(a)*i} ")
     
except Exception as e:   #syntax
   print(e)
# except:
#    print("invalid input")
### in except we give exception we want ---------
print("some imp lines of code")
print("End of program")
