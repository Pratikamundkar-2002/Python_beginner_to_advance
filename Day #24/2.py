
#-------------------operations/ methods on TUPLE--------------------------------------

countries =("spain", "India", "Italy", "England", "germany")
# this is a tuple, we can apply following steps to make changes in tuple

temp = list(countries)  # First convert 'tuple to list'.......(imp)

temp.append("Russia")   # russia is added in the end
temp.pop(3)        # index 3 is popped i.e deleted
#temp.insert(0,"berlin")    # inserts berlin on index 0, spain goes to index 1
temp[2] = "finland"

countries = tuple(temp)
print(countries)

print("............................................................................")
# we can add 2 tuples as a New Tuple
countries1 = ("pakistan", "afghanistan", "bangladesh", "srilanka", )
countries2 = ( "India","china", "Vietnam")
Asia = countries1 + countries2

print(Asia)
print(type(Asia))

print("-----------------------------------------------------------------------------")
# some METHODS

tuple = (0, 1, 3, 3, 2, 3, 1, 3, 2, 3)
print(tuple.count(3))  # counts occurance of 3 in tuple

res = tuple.index(2) #here it dos not print index[2], it prints 2's index i.e [4] 
print(res)

print(len(tuple))    # prints length of tuple


# WE CAN USE ALL LIST METHODS BY CONVERTING TUPLE INTO LIST AND RECONVERTING IT INTO TUPLE