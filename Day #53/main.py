
# map() reduce() filter()  functions:

# MAP() :-
# def cube(x):
#     return x*x*x
# # print(cube(2))
l= [1,2,4,6,3,2]
# newl =list(map(cube, l))
# print(newl)

# instead of writing above we use lambda function in one line
newl= list(map(lambda x : x*x*x, l))   #it will map the function(value) to the list
print(newl)


#-------------------------------------------------------------------------------------
# FILTER() :-
# def filter_function(a):
#     return a<4         # it will filter the elements that are less than 4
# newnewl = list(filter(filter_function, l))
# print(newnewl)

newnewl= list(filter(lambda x: x<4, l))  # lambda function with filter
print(newnewl)



#------------------------------------------------------------------------------------
# REDUCE() :-
from functools import reduce

numbers= [1,2,3,4,5]
add= list(reduce(lambda x, y: x+y, numbers)) # addition of above numbers
print(add)              # reduces the list by adding 
'''
1+2+3+4+5
3+3+4+5
6+4+5
10+5
15 == output
'''