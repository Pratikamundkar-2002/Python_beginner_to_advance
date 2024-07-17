
# Inheritence in Py---------------------------------------

#types= # Single Inheritence
        # multiple Inheritence
        # Multilevel Inheritence
        # Hierarichal Inheritance
        # Hybrid Inheritence

class employee:
    def __init__(self, name, id):
        self.name= name 
        self.id= id

    def showdetails(self):
        print(f"The name of Employee: {self.id} id {self.name}")

"""
assume this class is created already and is in use for long time,
someone arrives and say he want to change the class name----------------
So we use Inheritence
"""

class programmer(employee):  # this is a new class has all functions of class employee
    def showlanguage(self):
        print("Default language is python")

class baap(programmer):
    def the_end(self):
        print("The end")

e1= programmer("Rohan Das", 400) #instead of employee we write programmer the new created classs
e1.showdetails()
e1.showlanguage() # function of new class

e2= baap("mohan das", 500)
e2.showdetails()
e2.the_end()


