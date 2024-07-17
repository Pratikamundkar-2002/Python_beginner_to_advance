
# Access modifiers ----------------------------------------------------

class employee():
    def __init__(self):
        self.__name= "harry"    # _ _ name is used to give indication that it is private

a= employee()
print(a._employee__name)


 #--------------------------------------------------------------------------------------
        
class student:
    def __init__(self):
        self._name="harry"

    def _funName(self):
        return "code with harry"
    
class subject(student):
    pass

obj=student()
obj1=subject()
print(dir(obj))

print(obj._name)
print(obj._funName())

