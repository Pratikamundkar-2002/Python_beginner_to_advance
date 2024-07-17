
with open('newfile51.txt', 'r') as f:
 print(type(f))  # type of file

 f.seek(10) # it will move to the 10th byte in file     # seek() function
 data = f.read(9)  #read next 9 bytes after seek
 print(data)  # and print them




# with open('newfile51.txt', 'r') as f:
#  data= f.read(10)
#  current_position= f.tell()                  #tell() function
#  f.seek(current_position)
#  print(data)



with open('newfile51.txt', 'w') as f:
 f.write('Hello boy!')                 # truncate() functon
 f.truncate(7) # it will Write 7 characters in thw file
