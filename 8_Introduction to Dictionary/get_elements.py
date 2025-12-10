# No position things is in Dictionary. Use key to get value of that key

my_dict = {"name": "Rupesh","age": 23, "gender": "Male"}

# -------- Method1 --> To get a value 

print(my_dict["name"]) # Rupesh
print(my_dict["age"])  # 23
#print(my_dict["xyz"]) # KeyError: 'xyz' as it doesn't exist in my_dict

# ---------- Method 2 --> To get a value using get

r = my_dict.get("gender")
print(r) # Male

t = my_dict.get("class")
print(t) # None
print(type(t)) # <class 'NoneType'>



# -------- Ques: Enetr a key if it exist in my dictionary print "Rupesh" if not then print key doesn't exist

k = input("Enter a key: ")
result = my_dict.get(k)
if result is not None:
    print(result)
else:
    print("key does not exists")