
# Static methods in py ---------------------------------------------------------------

class Math:
    def __init__(self, num):
        self.num= num

    def addtonum(self, n):
        self.num = self.num +n
       
    @staticmethod       # satic method does not belong to class or instance-()
    def add(a,b):       # here we dont need to give (self) Argument
        return a+b
    
a= Math(5)
print(a.num)

a.addtonum(6)
print(a.num)

# print(Math.add(7,12))
a=Math.add(3,2)
print(a)
# --------------------------------------------------------------------------


class Good:
    @staticmethod  # here we dont need to take   __init__(self)
    def sub(a,b):
        return a-b
    
c= Good.sub(9, 3)
print(c)