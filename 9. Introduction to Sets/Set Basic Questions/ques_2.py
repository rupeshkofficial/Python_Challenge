"""
Python program to find common elements in three list using sets.
"""

list1 = [3, 6, 7, 5, 55, 3, 1, 2, 2, "Python", "Rupesh"]
list2 = [7, 8, 5, 6, 1, "Rupesh"]
list3 = [1, 1, 1, 2, 3, 4, 5]

# set1 = set(list1)
# set2 = set(list2)
# set3 = set(list3)

# x = set1.intersection(set2)
# result = x.intersection(set3)
# print(result) # {1, 5}

print(set(list1) & set(list2) & set(list3)) #  {1, 5}