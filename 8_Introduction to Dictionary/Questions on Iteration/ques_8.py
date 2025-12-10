"""
Store "name" of a student as key, "list of 5 marks of that student as a value. Store atlest 5 student names. print the name of the students. who got highest marks.
"""

students_data = {
    "Student1" : [85, 90, 78, 92, 88],
    "Student2" : [75, 88, 92, 80, 87],
    "Student3" : [90, 95, 89, 78, 93],
    "Student4" : [80, 85, 88, 92, 87],
    "Student5" : [92, 88, 95, 90, 85]
}

highest_marks = 0
highest_student_name = ""

for name,marks in students_data.items():
    total = sum(marks)
    if total > highest_marks:
        highest_marks = total
        highest_student_name = name
print(highest_student_name)
print(highest_marks)
