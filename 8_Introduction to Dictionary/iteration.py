my_dict = {"name": "Rupesh","age": 23, "gender": "Male", "Company": "Rupesh Tech"}

#print(my_dict.keys()) # dict_keys(['name', 'age', 'gender', 'Company'])

# ----------- Iterating Over keys to print key------------
for k in my_dict.keys():
    print(k, end = " ") # name age gender Company

# ---------- Method 1 --> Iterating over keys to print values

for k in my_dict.keys():
    print(my_dict[k], end = " ")  # Rupesh 23 Male Rupesh Tech

# ----- Method 2

for k in my_dict.values():
    print(k, end = " ")  # Rupesh 23 Male Rupesh Tech
