"""
Ask subject Name and Marks from the user and keep adding it to dictionary.
"""

marks = {}
subject_count = int(input("Enter how many subjects: "))

for _ in range(0,subject_count):
    subject_name = input("Enter subject Name = ")
    subject_marks = int(input(f"Enter marks for {subject_name} = "))
    #marks[subject_name] = subject_marks
    marks.update({subject_name : subject_marks})
print(marks)