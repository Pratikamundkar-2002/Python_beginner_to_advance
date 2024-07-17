''' Create a program capable of greeting you with God Morning, Good Afternoon
 and Good Evening.
 Your program should use time module to get current hour

 '''

import time
t= time.strftime ('%H: %M: %S')
hour = int(time.strftime('%H'))
hour = int(input("If the time is:"))
print(hour)


if (hour>0 and hour<=12):
    print('Good Morning')

elif (hour>12 and hour<16):
    print('Good Afternoon')

elif (hour>15 and hour<22):
    print('Good Evening')

else :
    print("Good night")