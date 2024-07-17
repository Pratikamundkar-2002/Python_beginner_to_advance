
# Magic / Dunder Methods --------------------------------------------------------

from emp import employee

e=employee("harry")
print(str(e))
print(repr(e))

e()  # this will print __call__ method
