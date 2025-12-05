"""
mom ======> mom
abc ======> cba
noon ======> noon
"""

my_sting = input("Enter a string = ")

if my_sting == my_sting[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")