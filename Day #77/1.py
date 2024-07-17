
# Operator Overloading _------------------------------------------

class vector:
    def __init__(self, i, j, k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):     # this is method overriding
        return vector(self.i +x.i, self.j +x.j, self.k +x.k) # add operator adds the + symbol
    
v1=vector(3,5,6)
print(v1)

v2= vector(1,3,4)
print(v2)

# now if we have to add v and v2 :
print(v1 + v2)        # this will give error so we have to add a  __add__() function
