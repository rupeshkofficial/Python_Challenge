my_set1 = {45, 43, 12, 43, 67, 78, 45, 43}
my_set2 = {43, 78, 909, 876, 543}


# Union --> Combine both sets and remove duplicates
print(my_set1.union(my_set2)) # {67, 43, 12, 45, 78, 876, 909, 543}

# Intersection --> Comman elements between two sets
print(my_set1.intersection(my_set2)) # {43, 78}
