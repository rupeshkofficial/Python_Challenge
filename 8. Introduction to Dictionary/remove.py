my_dict = {"name": "Rupesh","age": 23, "gender": "Male", "Company": "Rupesh Tech"}
print(my_dict) #{'name': 'Rupesh', 'age': 23, 'gender': 'Male', 'Company': 'Rupesh Tech'}

# ------- Method 1 --> Using del | del can be used for list and dictionary also

del my_dict["gender"]
print(my_dict) #  {'name': 'Rupesh', 'age': 23, 'Company': 'Rupesh Tech'}


#del my_dict      # Here i have deleted the variable not key value pair so, when i will print my_dict it will give KeyError
#print(my_dict)   # NameError: name 'my_dict' is not defined    



# ---------- Method 2 ( Using Pop)

my_dict.pop("name")
print(my_dict) # {'age': 23, 'Company': 'Rupesh Tech'}


# ---------- Tasks 1 ( What will happen if i use my_dict.pop() )
#my_dict.pop()
#print(my_dict) # TypeError: pop expected at least 1 argument, got 0

# --------- Tasks 2 ( How i will use popitem() )
my_dict.popitem()
print(my_dict) # 'age': 23}