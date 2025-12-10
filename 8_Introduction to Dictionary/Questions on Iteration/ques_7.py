"""
Store marks of 5 different subjects in a dictionary. Ask subject name
as an inpuit from the user. Print the marks of that subject entered by user.
if subject does not exist, print "Invalid".
"""

subject_marks_dict = {
    "Maths": 90,
    "English": 85,
    "Science": 92,
    "History": 88,
    "Computer Science": 95,
}

subject_name = input("Enetr subject Name = ")

if subject_name in subject_marks_dict:
    print(subject_marks_dict[subject_name])
else:
    print("Invalid")