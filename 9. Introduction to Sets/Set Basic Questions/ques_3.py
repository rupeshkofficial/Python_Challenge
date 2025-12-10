"""
Create three sets of your own, find the union of three sets.
"""

list1 = [3, 6, 7, 5, 55, 3, 1, 2, 2, "Python", "Rupesh"]
list2 = [7, 8, 5, 6, 1, "Rupesh"]
list3 = [1, 1, 1, 2, 3, 4, 5]



print(set(list1) | set(list2) | set(list3)) #  {1, 2, 3, 'Python', 5, 6, 7, 8, 4, 'Rupesh', 55}