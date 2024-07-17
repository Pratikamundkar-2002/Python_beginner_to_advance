
# Super keyword in python-----------------------------------

class Parent:
    def parent_method(self):
        print("this is a parent method")

class Child(Parent):
    def parent_method(self):  # we can define parent class in child
        print("Pratik")
        super().parent_method()

    def child_method(self):
        print("this is  child method")
        super().parent_method()    # this will take parent method of its parent class
    

child_object=Child()
child_object.child_method()
child_object.parent_method()
# parent_object=Parent()