
cities1= {"tokyo", "madrid", "berlin","delhi"}
cities2= {"tokyo", "delhi"}

#disjoint means there should not be a single intersection
print(cities1.isdisjoint(cities2))
#-------------------------------------------------------------------------------

# superset means c1 includes all values in c2 so c1 is superset of c2
print(cities1.issuperset(cities2)) 
#-------------------------------------------------------------------------------

# c1 is not subset of c2 so it is FALSE
print(cities1.issubset(cities2))
#-------------------------------------------------------------------------------

cities2.add("helsenki")
print(cities2)

cities1.update(cities2)  # c2 will be ADDED in c1
#-------------------------------------------------------------------------------

cities1.remove("delhi")  
print(cities1)
#cities1.remove("delhi23")    #here it will show error as delhi23 is not in c1
#print(cities1)

cities1.discard("delhi1") # will not show error,as delhi1 is not present in c1
print(cities1)
#----------------------------------------------------------------------------

states ={"maharashtra", "punjab", "haryna", "karnataka"}

print(states.pop())   # it pops a random value and prints it

#del states    # deletes the entire set

#if we dont want to delete set,instead we just want to clear it and make it empty..
states.clear()
print(states)
#------------------------------------------------------------------------------------

info ={"maharashtra", "punjab", "haryna", "karnataka"}
if 'punjab' in info:
    print("Yes, present")
else:
    print("Not present")