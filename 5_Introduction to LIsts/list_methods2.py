a = [1, 2, 3, 4, 5, "Rupesh", True, 55.67, -95]

# index
pos = a.index("Rupesh")
print(pos)

# sort
b = [44,45,67,89,34,57,33]
b.sort()
print(b)

c = ["Rupesh","Raju","Raja","Ram"] 
c.sort() # Sorted on the basis os ASCII Code
print(c)

# reverse
b.reverse()
print(b)

# For Descending Order --> First sort then it will be in ascending order then reverse then it will be in descending order
t = [23,45,67,34,56,24]
print(t)
t.sort()
t.reverse()
print(t)

#For Easy way to n descending order
p = [23,45,67,34,56,24,90,45,344]
p.sort(reverse=True)
print(p)


# Append --> Added the data at the end of the list. if list then directly added list at the end of the list
# Extend --> Added the element of the list at end of the another list

r = [1, 2, 3, 4, 5, "Rupesh", True, 55.67, -95]
#r.append(["Ram","Shyam",23,45,22,67,23.4])
#print(r) # O/P: [1, 2, 3, 4, 5, 'Rupesh', True, 55.67, -95, ['Ram', 'Shyam', 23, 45, 22, 67, 23.4]]
r.extend(["Ram","Shyam",23,45,22,67,23.4])
print(r) # O/P: [1, 2, 3, 4, 5, 'Rupesh', True, 55.67, -95, 'Ram', 'Shyam', 23, 45, 22, 67, 23.4]


# Count --> Count the no fo value occurance.
t = [23,45,67,3,7,437,3,7,3,6,24,67,5]
total = t.count(3)
print(total) # # occurs 3 times so, output will be 3.

# Clear
p = [23,45,67,3,737,34,7,43,6,24,67,5]
p.clear()
print(p) # List will be there but all the elements inside the list will be removed. So, Only print empty list. O/P: []


