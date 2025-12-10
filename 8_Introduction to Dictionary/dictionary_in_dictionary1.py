students_data = {
    "anirudh": {
        "roll_number": 431,
        "gender": "Male",
        "physics": 78,
        "chemistry": 89,
        "maths": 67,
    },
    "sanjay": {
        "roll_number": 122,
        "gender": "Male",
        "physics": 90,
        "chemistry": 75,
        "maths": 82,
    },
    "raj": {
        "roll_number": 786,
        "gender": "Male",
        "physics": 82,
        "chemistry": 91,
        "maths": 56,
    },
}

#print(students_data)
#print(type(students_data))

# print(students_data["anirudh"]) # It is a dictionary
# print(students_data["anirudh"]["roll_number"]) 

for name,details in students_data.items():
    total = details["physics"] + details["maths"] + details["chemistry"]
    gender = details["gender"]
    print(f"{name} -> {total}, gender = { gender}")