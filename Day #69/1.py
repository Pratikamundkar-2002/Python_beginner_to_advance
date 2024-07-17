
# Class methods -------------------------------------------------------------

class employee:
    company = "Apple"

    def show(self):
        print(f" name is {self.name} and company is {self.company}")

    @classmethod  # this decorator/method will take cls as a class employee:

    def changecompany(cls, newcompany): # instead of self we can write any thing like-(cls)
        cls.company= newcompany # here we change the clas employee.company to newcompany

e1= employee()
e1.name= "Pratik"
e1.show()
e1.changecompany("Tesla")
e1.show()
print(employee.company) #Apple will be printed if we dont give @classmethod


# simply @classmethod class uplabd karun deto instead of self ani apan class variable 
# change karu shakto