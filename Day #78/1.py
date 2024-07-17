
# Inheritence--------------------------------------

# Single inhertence :- class inherit properties from single parent class

class animal:
    def __init__(self, name, species):
        self.name=name
        self.species=species

    def makesound(self):
        print("Sound made by animal")

class dog(animal):
    def __init__(self,name, breed):
        animal.__init__(self,name,species="Dog")
        self.breed=breed

    def makesound(self):
        print("Bark")

d=dog("Dog", "husky")
d.makesound()

a=animal("Dog", "Dog")
a.makesound()
