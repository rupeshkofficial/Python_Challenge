
# Question 1
my_dict = {"history": 15, "maths": 99, "computer": 75, "geo": 26}

total_marks = 0

for v in my_dict.values():
    total_marks = total_marks + v
print(total_marks)  # 215


# --------------- Question 2

my_dict1 = {"name": "Rupesh","age": 23, "gender": "Male", "Company": "Rupesh Tech"}

print(my_dict1.items()) #dict_items([('name', 'Rupesh'), ('age', 23), ('gender', 'Male'), ('Company', 'Rupesh Tech')])

for k,v in my_dict1.items():
    print(f"{k} -> {v}")