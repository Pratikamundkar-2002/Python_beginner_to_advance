
# Getters and Setters in py -------------------------------------------------

class myclass:
    def __init__(self, value):
        self._value = value
    
    def show(self):
     print(f"Value is {self._value}")

    @property            #This is used to get a value. This act as getter  
    def ten_value(self):
        return 10* self._value 
    
    @ten_value.setter    #This is used to set/change a value. This act as setter
    def ten_value(self, new_value):
       self._value = new_value/10

obj= myclass(10)
obj.show()

obj.ten_value =67
print(obj.ten_value)
