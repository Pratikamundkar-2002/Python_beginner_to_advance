

from typing import Any


class employee:
    def __init__(self, name):
        self.name=name

    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    
    def __str__(self):             
        return f"Employee 1 {self.name}" # if we del this it will fall back to repr if self is not found
    
    def __repr__(self):     
        return f"Employee 2 {self.name}"   # if we write this still it will print str but ^
    
    def __call__(self):
        print("Hey i am good")
    
