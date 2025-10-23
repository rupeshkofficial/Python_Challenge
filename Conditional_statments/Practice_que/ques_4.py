""" To check last digit of a number is divisible by 5 or not"""

num = int(input("Enter any number: "))
last_digit = num%10

if last_digit%5==0:
    print(f"last digit of {num} is divisible by 5")
else:
    print(f"last digit of {num} is not divisible by 5")