# Ask two numbers X and Y from the user. if X < Y then print all the numbers from X to Y, but if Y < X then print all the numbers from Y to X.

x = int(input("Enter 1st Number: "))
y = int(input("Enter 2nd Number: "))

if x < y:
    i = x
    while i <= y:
        print(i, end = " ")
        i = i + 1
else:
    i = y
    while i <= x:
        print(i, end = " ")
        i = i + 1

  

