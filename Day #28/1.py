
# String Formatting in python ------------------------------------------------------------------

letter = "hey my name is {1} and I am from {0}"
country= "India"
name= "Pratik"

print(letter.format(country, name))  # this method is so hard if there are so many values

#So we use  f-string
print(f"hey my name is {name} and I am from {country}")

print("-----------------------------------------------------------------------")
price =49.09888823
# text = f"for only {price:.2f} dollars! "   # prints 2 decimal after point
# print(text)
print(f'%.2f'%price)                   # prints 2 decimal after point

print("-------------------------------------------------------------------------")
print(f"{3 * 10}")       # this will be printed as a string
print(type(f"{3 * 10}"))

