x = int(input("Enter a number: "))
count = 0

while x > 0:
    count = count + 1
    x = x // 10
print("Number of digits:", count)