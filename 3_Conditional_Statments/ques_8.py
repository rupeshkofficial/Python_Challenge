'''
Calculate Percentage and print it as well as their grade also.

91 - 100 --> A
81 - 90 --> B
71 - 80 --> C
61 - 70 ---> D
1 - 60 ---> Fail
Invalid

'''

sub1 = int(input("Enter sub1 Marks: "))
sub2 = int(input("Enter sub2 Marks: "))
sub3 = int(input("Enter sub3 Marks: "))
sub4 = int(input("Enter sub4 Marks: "))
sub5 = int(input("Enter sub5 Marks: "))

percentage = ((sub1 + sub2 + sub3 + sub4 + sub5) / 500) * 100
print(f"Your Percentgae is {percentage}")

if percentage >= 91 and percentage <= 100:
    print("Grade: A ")
elif percentage >= 81 and percentage <= 90:
    print("Grade: B")
elif percentage >= 71 and percentage <= 80:
    print("Grade: C")
elif percentage >= 61 and percentage <= 70:
    print("Grade: D")
elif percentage >= 1 and percentage <= 60:
    print("FAIL")
else:
    print("Invalid Percentage!")
