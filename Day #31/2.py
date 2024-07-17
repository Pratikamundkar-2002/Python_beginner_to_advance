
# set Methods ...............................................................

s1= {1,3,5,7,4}
s2= {2,4,6,1}
print(s1.union(s2))

s1.update(s2)  # s1 ke andar who values leke aao jo s2 me hai s1 me nahi
print(s1,s2)   # i.e {1,2,3,4,5,6,7}

#_----------------------------------------------------------------------------------

c1= {1,3,5,7,4}
c2= {2,4,6,1}
print(c1.intersection(c2))

c1.intersection_update(c2)
print(c1)

print("---------------------------------------------------------------------------")
# symmetric difference = (a Union b)- (a intersection b)
cities1= {"tokyo", "madrid","berlin", "delhi"}
cities2= {"tokyo", "seoul", "kabul", "madrid"}

cities3= cities1.symmetric_difference(cities2)  # it will print values do not intersect
print(cities3)

# difference 
cities4= cities1.difference(cities2)
print(cities4)