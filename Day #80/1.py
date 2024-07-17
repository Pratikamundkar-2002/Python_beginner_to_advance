
# Multilevel Inheritence :------------------------------
#parent class accessed by son and son accessed by his son

# class a()
# class b(a)
# class c(b) 

class animal:
    def __init__(self,name, species):
        self.name=name
        self.species=species
    def showdetails(self):
        print(f"name: {self.name}")
        print(f"species: {self.species}")
    

class dog(animal):
    def __init__(self,name, breed):
        animal.__init__(self,name,species="Dog")
        self.breed= breed
    def showdetails(self):
        animal.showdetails(self)
        print(f"breed: {self.breed}")
    

class goldenretriver(dog):
    def __init__(self, name, color):
        dog.__init__(self,name,breed="golden retriver")
        self.color=color
    def showdetails(self):
        dog.showdetails(self)
        print(f"color: {self.color}")
        
o=goldenretriver("tommy", "black")
o.showdetails()

z=goldenretriver("Ruby", "Golden")
z.showdetails()