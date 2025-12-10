# Mutable / Immutable Data Type

a = [54,23,10,99,-90]
# print(len(a))
# print(sum(a))
# print(max(a))
# print(min(a))
# print()
# id
# range

#print(a)

# append
a.append(100) # Added at last of list
a.append(-2100)
a.append("Rupesh")

# insert
a.insert(3,"Code") # Code will be added at third position and the previous 3rd positin of elements will shift to 4th position
a.insert(0,"Python") # Python will be added at Zeroth position and the previous Zeroth positin of element will shift to 1st position
a.insert(400,"Raja") # If position not exist then element will be added at last position by default

# update
a[0] = 100 # Just update the Zeroth position elements with 100
a[-1] = 100
#a[50] = 200  #IndexError: list assignment index out of range

# pop (Remove by Index)
a.pop() # By default last elements from list will be deleted
a.pop()
a.pop(0) # Zeroth position element will be deleted ( Pop removed by index)
print(a)

# remove ( Remove by Value)
a.remove(23) # If two 23 exist in list then only 1st 23 will removed and 2nd will  not be removed
# a.remove(500) # ValueError: list.remove(x): x not in list ( As value not exist in list)
print(a)

# del ( Delete by Index)
del a[0] # Zeroth position elements will be deleted
#del a  # list will be deleted
print(a)

# Clear ( All elements in list will be clear but list will be empty)
a.clear()
print(a)