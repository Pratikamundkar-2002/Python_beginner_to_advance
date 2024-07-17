
# dir(), __dict__, help() methods in py--------------(built in functions)

x=[1,2,3]
print(dir(x))
# print(x.__add__)

# __dict__
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=person("John", 30)
print(p.__dict__)  # this will print in form of dictionary
    
# help()
print(help(person)) #gives help documentation for person