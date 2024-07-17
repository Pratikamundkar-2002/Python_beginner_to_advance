
# multiple inheritence :=-------------------------------------
# 1 child class has multiple parent class

class employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"The name is {self.name}")    
    

class dancer:
    def __init__(self, dance):
        self.dance=dance
    def show(self):
        print(f"The dance is {self.dance}")    
    

class danceremployee(employee, dancer): # here employee is written first so,,,
    def __init__(self,dance,name):
        self.dance =dance
        self.name =name

o=danceremployee("hiphop", "Shivani")
print(o.name)
print(o.dance)
o.show()  # this will print from employee and not dancer