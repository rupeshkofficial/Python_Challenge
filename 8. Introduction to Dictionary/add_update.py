my_dict = {"name": "Rupesh","age": 23, "gender": "Male"}

print(my_dict)    # {'name': 'Rupesh', 'age': 23, 'gender': 'Male'}


# ------- Method 1 ( If key exist then update if key not exist then it will add)

# Example ( Key Exist --> Update)
my_dict["age"] = 100 
print(my_dict)   # {'name': 'Rupesh', 'age': 100, 'gender': 'Male'}

# Example ( Key not Exist --> Added)
my_dict["xyz"] = 234
print(my_dict) # {'name': 'Rupesh', 'age': 100, 'gender': 'Male', 'xyz': 234}