"""
Ask 4 number from user. Make sure all the numbers entered by user are different. Print which number is the smallest.
"""

x1 = int(input("Enter 1st Number: "))
x2 = int(input("Enter 2nd Number: "))
x3 = int(input("Enter 3rd Number: "))
x4 = int(input("Enter 4th Number: "))

if x1<x2 and x1<x3 and x1 < x4:
    print(f"1st Number {x1} is smallest")
elif x2<x1 and x2<x3 and x2 < x4:
    print(f"2nd Number {x2} is smallest")
elif x3<x1 and x3<x2 and x3 < x4:
    print(f"3rd Number {x3} is smallest")
else:
    print(f"4th Number {x4} is smallest.")