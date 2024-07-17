
# class methods as alternative constructors =--------------------------------------->

class employee:
    def __init__(self, name, salary):
        self.name= name 
        self.salary= salary

    @classmethod
    def fromstr(cls, string):   # this is alternat external constructor
        return cls(string.split("-")[0], string.split("-")[1])

e1=employee("harry", 12000)
print(e1.name)
print(e1.salary)

# but if we get data in form of string and we want to seperate the data-----
string="pratik-10000"
# e2=employee(string.split("-")[0], string.split("-"[1])) #we need to write for every string
e2=employee.fromstr(string)
print(e2.name)
print(e2.salary)
# This will be so lengthy so we use alternate,external Constructor



#example2 -
class student:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    
    @classmethod
    def fromStr(xz,string2):
        return xz(string2.split("_")[0], string2.split("_")[1])

string2="Pratik_22"
e3=student.fromStr(string2)
print(e3.name)
print(e3.age)