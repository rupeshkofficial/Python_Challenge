""" To check number is divisible by 2 and 3 but not not by 8"""

x = int(input("Enter a number: "))

if x % 2 == 0 and x % 3 == 0 and x%8 != 0:
    print("Yes, Number is divisible by 2 and 3 but not 8")
else:
    print("No")
