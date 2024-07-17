
# Break and Continue Statments------------------------------------------------

for i in range(12):   # here range is 12 but
    if(i == 10):      #here we apply break statement at 10
        break         # so it will print table till 10 i.e (5*10=50)
    print("5 *", i, "=",5* (i+1))

#------------------------------------------------------------------------------

for i in range(12):   # here range is 12 but
    if(i == 10):  
        print("-")    #here we apply continue statement at 10
        continue      # so when i=10 it will print - for that and continue the iteration till 12)
    print("5 *", i, "=",5* (i+1))   

#----------------------------------------------------------------------------------------


for i in[2,3,4,6,5,8,0,]:
    if(i%2 !=0):     # here if reminder is not equal to 0 it will skip that and continue further
        continue     # means it will print numbers dividible by 2
    print(i)


#-------------------------------------------------------------------------------------
#  Q. EMULATE DO-WHILE LOOP

i=0                 #here we took i=0 first
while True:     
    print(i)        #it will print 0
    i= i+1          #add +1 ie. 0+1=1
    if(i%100 ==0):  #check this condition, remainder is not zero, again repeat
        break
