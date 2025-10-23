""" To check no is Odd, Even or Zero."""

x = int(input("Enter any number: ")) # In python 0 % 2 = 0 (Remainder)

if x == 0:  
    print("Number is Zero")
elif x % 2 != 0:
    print("Number is Odd")
else:
    print("Number is Even")