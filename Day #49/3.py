# readline() and redlines() 

with open('myfile49.txt') as f:
    lines=f.readlines()
    for line in lines:
        print(line, end='') #this prints all the lines in the file with a gap of blank line
               # end='' is used to remove the gap between lines



with open('myfile49.txt') as f:
    single_line=f.readline() # reads a single line (first line)
    single_line2=f.readline() # reads a second line
               
    print(single_line)
    print(single_line2)
   


# we can also read certain amount of characters in a line-----------------------------
reader_amount=10
with open('myfile49.txt') as f:
    f.read() #here if we want to read the entire file and then certain characters atatime
    f.seek(0) #we should use seek method to do so or nothing will be printed

    content=f.read(reader_amount) # we can set amount and print certain characters
    content2=f.read(reader_amount) # ***prints next 10 characters
    print(content)
    print(content2)
# seek(0) will seek to first character after f.read() and again read the,
#  content and content2
