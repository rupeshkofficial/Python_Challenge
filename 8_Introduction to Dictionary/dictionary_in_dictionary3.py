students_data = {
    "anirudh": {
        "roll_number": 101,
        "gender": "Male",
        "marks": {"physics": 78, "maths": 89, "chemistry": 67},
    },
    "sara": {
        "roll_number": 102,
        "gender": "Male",
        "marks": {"physics": 90, "maths": 75, "chemistry": 82},
    },
    "alex": {
        "roll_number": 103,
        "gender": "Male",
        "marks": {"physics": 82, "maths": 91, "chemistry": 56},
    },
}

for name, details in students_data.items():
    #print(name)
    # print(details)
    # print(details["marks"]["physics"])
    # print(details["marks"]["chemistry"])

    total = (
        details["marks"]["physics"]
        + details["marks"]["chemistry"]
        + details["marks"]["maths"]
    )

    print(f"{name} has scorde {total} marks")