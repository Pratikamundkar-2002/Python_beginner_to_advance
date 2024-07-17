# ____ LOOPS in PYTHON_______________________________

name = "pratik"
for i in name:
    print(i)
    if(i=="r"):
        print("this is special")

# ___________________________________________________________________________

colors= ["red","green",'yellow',"blue"]

for color in colors:
    print(color)
    for i in color:
        print(i)

#______________________________________________________________________________

for k in range (5):
    print(k)       # it will print 0 to 4
    print(k+1)  # it will print 0 to 5

for k in range (1, 9):
    print(k)     # it will print till 8 from 1 , 9 is not included

for i in range( 1, 2001):
    print(i)

#_________________________________________________________________________

''' Range here has 3 parameters (start, stop, increment)
 means- range (1,12,3)
 here, 1 to 12 is a range and 3 is (skips) increment of 3.s
 like output- 1,4,7,10 (print 1 , after that print 3rd no. after 1, i.e 4 and so on till 12)
 3 IS CALLLED AS "INCREMENT"........
'''
for i in range(1,12,3):
    print(i)


