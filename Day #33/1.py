
 # Dictionaries in Python---------------------------------------------------------
# .......it is a combination key-value pairs...........

dict={
    "harry": "human",
    "spoon": "object"   # key-value pairs
}
print(dict["harry"])

#we can store rollno. of students and access
dict={
   12:"pratik",13:"omkar",
   14: "nirmal", 15:"dipak",
   16:"raj", 18:"suraj"
}
print(dict[15])
print("---------------------------------------------------------------------------")


# methods to access vlaues in  dict
info={"name":"karan", "age":21, "eligible":True}

print(info)       
print(info["name"]) 
# print(info[name1]) # this will throw error if key is not present

print(info.get("name"))  
# print(info.get("name"))# this will print 'none' if key is not present
#..........................................................................

print(info.keys())    # will access all key with dict name
print(info.values())  # will access all vlaues with dict name
print("------------------------------------------------------------------------------")


for key in info.keys():
    print(info[key])       #will iterate one by one value in ordered way

    print(f"the values corresponding to key {key} is {info[key]}") # using f-string

#---------------------------------------------------------------------------------
print(info.items()) #will access key-value pairs

for key, value in info.items():
    print(f"the value corresponding to {key} is {value}")

 