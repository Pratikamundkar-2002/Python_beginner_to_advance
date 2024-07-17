
# File Handling in python -------------------------------------------------------
# any text or binary file can be opened and various operations canbe performed
# read(), write(), append(), close(), 


# READING A FILE-- r is read Mode
f = open('my file.txt', 'rt') 
# (t) is used for TEXT FILE and (b) is used for BINARY fILE
text = f.read() # read a file
f.close() # we should close a file when it is opened


# WRITING A FILE-- w mode
f = open('myfile49.txt', 'w') # my file 2 is created as a new file
f.write('Helllo, World!') # This is written in the file
# #if we open a file in write mode which not exist, it is created as new file
# f.close

#we can use with statement which automatically close the file 
with open('myfile49.txt', 'a') as f:
    f.write("I am good")

# If a file already contains something in it and we want to write something in it
# if we open that file as write the original content will be deleted and only
# that will be stored that we wanted to write
# SO WE USE APPEND TO FILE-- a mode
with open('myfile.txt', 'a') as f:
    f.write("the topic is FILE HANDLING")
