
# FOR LOOP WITH ELSE ----------------------------------------------

''' condition- else is printed only when for loop is successfully ended, and reached
 till last value/iteration in loop'''

for i in range(5):
    print(i)
else:
    print("sorry no i") # here else is printed becoz for loop is fully executed

for i in range(5):
    print(i)
    if i==3:
        break        #here loop is break in the middle & all values are not executed
else:                #so else will not print here
    print("sorry no i")

print("----------------------------------------------------------------------------")

#  WE CAN ALSO TAKE WHILE LOOP WITH ELSE=--->
i=0
while i<7:
    i=i+1
    print(i)
else:
    print("sorry no i")

print("--------------------------------------------------------------------------")

for x in range(5):
    print("iteration no {}" .format(x+1))    #f-string
else:
    print("out of loop")