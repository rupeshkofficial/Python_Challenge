my_tuple = (54,87,74,41,52)

my_list = list(my_tuple)
print(my_list)

my_list.append(100)
print(my_list)

my_tuple = tuple(my_list) # Overriding here on tuples.
print(my_tuple)