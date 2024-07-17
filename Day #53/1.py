
from functools import reduce 

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
my_numbers = [4, 6, 9, 23, 5]

# square the float and obtain result with 3 decimal points
map_result = list(map(lambda x: round(x ** 2, 3), my_floats))
print(map_result)

# print names that are less than or equal to 7 letters
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
print(filter_result)

# product of all numbers *
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)
print(reduce_result)
