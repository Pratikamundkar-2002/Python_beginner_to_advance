#for append 'a' is used

with open('myfile49.txt', 'a') as f:
    f.write('\n')   #append on new line
    f.write("the topic is FILE HANDLING")
    


with open('myfile49.txt', 'r') as f:
    content=f.read()

print(f.name)  #will print file name
print(f.closed) #true if closed or false
print(f.mode)  # will print mode of file
print(len(content)) #will print length of content in a file
