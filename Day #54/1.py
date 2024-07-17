
# '==' VS 'is' in py
# "is" will be true when the identity is same
# "==" will be true when value is exactly same

a=12
b='10'
print(a==b)    # value 
print(a is b)  # exact location of object in memory


c=[1,2,3,4]
d=[1,2,3,4] # crate a list
print(c==d) #True
print(c is d) #False becoz seperately stored in memory
# like same model(iphone) but two diff mobiles


e=3
f=3
print(e==f) # True
print(e is f) # True becoz 3 will be stored only once in memory at a location
 
 
i="pratik"
j="pratik"
print(i==j) # True
print(i is j) # True