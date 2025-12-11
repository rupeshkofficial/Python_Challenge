"""
Write a python program to find elements in a given set that are not in another set.
"""

set1 = {5, 6, 2, 1, "Rupesh", 7}
set2 = {"Python", 76, 22, 91, -991, 7}

# set subtraction (set1 - set2) automatically returns all elements from set1 that do not appear in set2.
difference = set1 - set2

print("Elements in set1 but not in set2:", difference) # Elements in set1 but not in set2: {1, 2, 5, 6, 'Rupesh'}
