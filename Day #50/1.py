
# READ LINE () METHOD----------------------------------------------------------
# f = open('readfile50.txt', 'r')
# i=0
# while True:
#     i=i+1
#     line = f.readline()
#     if not line:
#         break
#     m1= int(line.split(",")[0])  #If there is comma split .
#     m2= int(line.split(",")[1])
#     m3= int(line.split(",")[2])
#     print(f"marks of student {i} in maths is: {m1}")
#     print(f"marks of student {i} in english is: {m2*2}")
#     print(f"marks of student {i} in geography is: {m3}")
    
#     print(line)




# WRITE LINE () METHODS-----------------------------------------------------------
# f = open('readfile50.txt', 'w')
lines=[ 'line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()

with open('readfile50.txt', 'w') as f:
    f.writelines(lines)
