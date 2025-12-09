'''
----------------------- Index / Position in Lists -----------------------------

x = [45, 32, 15, "C&D", 198.88, 61]

     0   1   2    3      4      5 ---> Position representation in +ve 
     -6  -5  -4   -3     -2     -1 ---> Position representation in -ve 

length = 6 ( No. of elements in lists)
Position = 0 to 5

print(x[-2]) --> O/P : 4
'''

a = [55,43,12,"Rupesh","C&D",-98,99.55]

print(a)
print(a[1])
print(type(a[1]))

print(a[6])
print(a[-1])
print(a[-2])

#print(a[-10])     #IndexError: list index out of range

