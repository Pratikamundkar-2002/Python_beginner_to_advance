
#   LIST Comprenhension  --------------------------------------------------------(imp)
# means creating new another list from other iterables like list, tupule, dict, even str,array
lst= [i for i in range(4)]
print(lst)

lst= [i*i for i in range(4)]
print(lst)

lst= [i*i for i in range(10) if i%2==0]
print(lst)

lst= [i-2 for i in range(4,20) if i%2!=0]
print(lst)