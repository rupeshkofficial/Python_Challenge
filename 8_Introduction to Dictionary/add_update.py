my_dict = {"name": "Rupesh","age": 23, "gender": "Male"}

print(my_dict)    # {'name': 'Rupesh', 'age': 23, 'gender': 'Male'}


# ------- Method 1 ( If key exist then update if key not exist then it will add)

# Example ( Key Exist --> Update)
my_dict["age"] = 100 
print(my_dict)   # {'name': 'Rupesh', 'age': 100, 'gender': 'Male'}

# Example ( Key not Exist --> Added)
my_dict["xyz"] = 234
print(my_dict) # {'name': 'Rupesh', 'age': 100, 'gender': 'Male', 'xyz': 234}


# ------------ Method 2 ( Update ---> It needs dictionary) || if any key exist in previous dictionary and if we again add then it will updated with new one.

my_dict.update({"marks": 100 , "Address": "New Delhi"})
print(my_dict) # {'name': 'Rupesh', 'age': 100, 'gender': 'Male', 'xyz': 234, 'marks': 100, 'Address': 'New Delhi'}


my_dict.update({"marks": 100 , "Address": "New Delhi", "name":"Raja"})
print(my_dict) # {'name': 'Raja', 'age': 100, 'gender': 'Male', 'xyz': 234, 'marks': 100, 'Address': 'New Delhi'}
