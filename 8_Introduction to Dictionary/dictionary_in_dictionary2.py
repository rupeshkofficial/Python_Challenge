students_data = {
    "anirudh": {
        "roll_number": 431,
        "gender": "Male",
        "marks": [78, 89, 67, 92, 54],
    },
    "sara": {
        "roll_number": 122,
        "gender": "Male",
        "marks": [90, 75, 82, 68, 91],
    },
    "alex": {
        "roll_number": 786,
        "gender": "Male",
        "marks": [82, 91, 56, 78, 69],
    },
}

for name,details in students_data.items():
    total = sum(details["marks"])
    print(f"{name} has scorder {total} marks")