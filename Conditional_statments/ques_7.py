num1 = int(input("How many classes held: "))
num2 = int(input("How many classes you attended: "))

attendacne_per = (num2 / num1 ) * 100

print(f"Your attendance percentage is {attendacne_per}") # Your attendance percentage is 16.666666666666664
print(f"Your attendance percentage is {attendacne_per: .2f}") # To roundoff the percentage upto 2 decimal like 16.67

if attendacne_per > 75:
    print(f"Great! You are allowed to seat in exam as your attendacne percentage is {attendacne_per}")
else:
    print(f"Sorry! You are not allowd to seat in exam as your attendance percentage is {attendacne_per}")