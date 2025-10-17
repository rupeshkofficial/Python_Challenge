'''
IF-ELIF-ELSE Statments ---> To handle multiple conditions 
Note: ELSE condition isn't necessary to give here or you may take multiple elif.

Syntax:

if condition1:
    -----
    -----
elif condition2:
    ----
    -----
elif condition3:
    ------
    -----
else:
    -----

'''

# Code 1

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 > num2:
    print("Number 1 is greater")
elif num2 > num1:
    print("Number 2 is greater")
else:
    print("Both are equal")
