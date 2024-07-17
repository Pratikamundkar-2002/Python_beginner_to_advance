
#  List METHODS in py_________________________________________________________________

l= [18, 45, 2, 5 , 8, 10]
print(l)

l.append(4)
print(l)         # appends (adds) 4  to the end of list
#-------------------------------------------------------------------------
l.sort()        # sorts in ascending order
print(l)
l.sort(reverse=True)   # descending order
print (l)
#-------------------------------------------------------------------------
l1= [ 18, 45, 2, 5, 9, 10]
l1.reverse()
print(l1)     # reverse from 10 to 18
#-------------------------------------------------------------------------
l2= [ 18, 1, 2, 5, 9, 1]
print(l2.index(1))   #Tells the index of 1, by first managing in ascending order (i.e index=1)
print(l2.count(1))   # counts occurance of 1

l2.insert(1,199)  #insert 199 on index 1
print(l2)

m=[900, 1000, 1100]
l2.extend(m)      # concatinating (adding) m in l2
print(l2)
# or->  
# y=(m + l2)
# print(y)




