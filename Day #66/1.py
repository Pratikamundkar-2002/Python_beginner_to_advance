
# Instance variable Vs Class Variable in py ------------------------------------

class employee:
    CompanyName= "Apple"   # this is associated with class ie. Common for all employees
# so this is class variable , default for 
    noofemployees= 0  # if we want to know the no. of employees

    def __init__(self, name):
       self.name= name
       self.amount= 0.02
       employee.noofemployees +=1  # will show the no. whenever the new employees are added 

    def Showdetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.CompanyName} is {self.amount} with employees {self.noofemployees}")

emp1=employee("Harry") # this is instance variable
emp1.amount=0.3
emp1.CompanyName= "Apple India"  #If instance varible is available It takes this value for employee harry
emp1.Showdetails()

employee.CompanyName ="Google"  # if we add this it will print "Google" instead of class instance
print(employee.CompanyName) # this will print the Name of Company of class instance

emp2= employee("Rohan")
emp2.CompanyName="Accenture"
emp2.Showdetails()

# Shortly if instance variable is available it will take that
# or it will Search for Class variable 