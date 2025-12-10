my_set = {3, 4, 5, 6, 7}
print(my_set)

my_set.add(100)
print(my_set) # {3, 4, 5, 6, 7, 100}

my_set.add(7) # If 7 is already in set then it will do nothing. I mean 7 will not add again
print(my_set) # {3, 4, 5, 6, 7, 100}

my_set.remove(4)
print(my_set) # {3, 5, 6, 7, 100}

# It will give error if we remove any elements that doesn't exist in sets
# my_set.remove(1000)
# print(my_set) # KeyError: 1000 