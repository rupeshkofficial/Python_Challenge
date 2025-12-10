# Ask two numbers X and Y from the user. if X < Y then print all the numbers from X to Y, but if Y < X then print all the numbers from Y to X.

x = int(input("Enter 1st Number: "))
y = int(input("Enter 2nd Number: "))

if x < y :
    for i in range(x,y+1):
        print(i,end=" ")
else:
    for i in range(y,x+1):
        print(i,end=" ")
