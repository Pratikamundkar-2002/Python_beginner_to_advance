#----Q. Area of circle---------------------
#   area= 3.14*r*r

#import math------------# this is a math library with values or formulas

radius=float(input("Enter the radius of circle:"))
area= 3.14*radius*radius  
print("The area of circle is:", area)
 
#area= math.pi*radius*radius   both are correct

if(radius>0):
    area= 3.14*radius*radius  
    print("The area of circle is:", area)
# else:
    # print("Cannot find area of circle")    
   


