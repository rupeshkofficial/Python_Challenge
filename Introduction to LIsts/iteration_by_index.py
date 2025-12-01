'''
-------------------- Iterating through Lists -----------------------------

x = [45, 32, 15, "C&D", 198.88, 61]


print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

for i in range(0,5)
    print(a[i]) ---> i = 0 to 5


'''
# ------------------------------------------------------------
'''

# Iterate by Index/Position
a = [45, 32, 15, "C&D", 198.88, 61]
for i in range(0,6):
    print(a[i],end = " ")

'''
# ------------------------------------------------------------------

# a = [45, 32, 15, "C&D", 198.88, 61]
# x = len(a)
# print(x) --> 6

a = [45, 32, 15, "C&D", 198.88, 61]
for i in range(0,len(a)):
    print(a[i],end = " ")