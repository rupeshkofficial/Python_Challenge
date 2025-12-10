x = {"name": "Rupesh","age": 23, "gender": "Male"}
y = {"name": "Vishal", "age": 34, "gender": "Male"}
print(x)         # {'name': 'Rupesh', 'age': 23, 'gender': 'Male'}
print(y)         # {'name': 'Vishal', 'age': 34, 'gender': 'Male'}
print(type(x))   # <class 'dict'>

# ----------- Key will be unique in dictionary. But if it repeat then the last one will be the key

z = {"name": "Rupesh","age": 23, "gender": "Male", "name":"Priya"}
print(z) # {'name': 'Priya', 'age': 23, 'gender': 'Male'}

# ---------- Key will be any data type not only strinbg. It may be string,float,integer

t = {"name": "Rupesh","age": 23, "gender": "Male", "name":"Priya", 1: 23}
print(t) # {'name': 'Priya', 'age': 23, 'gender': 'Male', 1: 23}


t = {"name": "Rupesh","age": 23, "gender": "Male", "name":"Priya", 1: 23, [12,345,56,]: 22}
print(t) # TypeError: cannot use 'list' as a dict key (unhashable type: 'list')