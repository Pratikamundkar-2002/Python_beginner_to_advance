
# Python Class and Object :--------------------------------------------------

class person:
    name = "harry"                    #
    occupation = "Software Developer" # these are default values 
    networt = 10                      #
    def info(self):
        print(f"{self.name} is a professional {self.occupation}")

# self is that object where this method is called
# a.info() here method is called on a
# so self will be "a" similarly "b", "c....

a=person()
b=person()
c=person()
# a.name= "pratik"  # name value changed from harry to pratik
# print(a.name , a.occupation)

a.name= "pratik"            # values can be changed
a.occupation= "Engineer"

b.name=  "Nikita"
b.occupation= "HR"

c.name= "sagar"
c.occupation= "scientist"

a.info()
b.info()
c.info()
