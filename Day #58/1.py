
# Constructors in py------------------------------------------------------------
# Constructors are used to create objects

#Default Constructor :-
class person:
    def __init__(self):  #init Method, this will be invoked everytime object will be created
        print("Hey I am a person")# this is printed whenever the object is created

    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person() # Object is created
b=person() # Object is created

a.name= "pratik"
a.occ= "engineer"
a.info()

print("----------------------------------------------------------------------------")

# Parameterized Constructor
class person:
    def __init__(self, name, occ):  # Variable Will be assigned to self
        print("Hey I am a person")
        self.name=name
        self.occ=occ

    def info(self):
            print(f"{self.name} IS A {self.occ}")

a=person("harry", "Developer") # these values will be assigned to n & o
b=person("Divya", "HR")

a.info()
b.info()


