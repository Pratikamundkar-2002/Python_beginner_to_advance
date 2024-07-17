marks= [3,5,6, 'pratik', True]
print(marks)

print(marks[-3])  # this is negative index, count reverse, here starting index is 1
print(marks[len(marks)-3]) # this is positive index
print(marks[5-3])
print(marks[2])
# in all above cases it will print 6.
#---------------------------------------------------------------------------------
# to check whether an item is present in list
if 6 in marks:
    print("YES")
else:
    print("NO")
#.....................................................

if "pra" in "pratik":
    print("ok")