

my_list = ["abc", "xyz", "hello", "Rupesh"]

print(my_list) # ['abc', 'xyz', 'hello', 'Rupesh']

my_string = " ".join(my_list) # Join by spaces

print(my_string) # abc xyz hello Rupesh

print(type(my_string)) # <class 'str'>


my_list1 = ["abc", "xyz", "hello", "Rupesh"]

my_string1 = "_".join(my_list1) # Join by hyphen

print(my_string1) # abc_xyz_hello_Rupesh

#------------------------------------------------------

# In Join every elements should be string not integer. If you give integer it will give error

# my_list = ["abc", "xyz", "hello", "Rupesh", 74]

# print(my_list) # ['abc', 'xyz', 'hello', 'Rupesh',74]

# my_string = " ".join(my_list) # Join by spaces

# print(my_string) # TypeError: sequence item 4: expected str instance, int found


# ----------------------------------------

my_list = ["abc", "xyz", "hello", "Rupesh", 74]

my_string1 = " ".join(str(i) for i in my_list)

my_string2 = " ".join(str(i) [::-1]for i in my_list) # Har ek word ulta jud jayega

print(my_string1) # abc xyz hello Rupesh 74

print(my_string2) # cba zyx olleh hsepuR 47