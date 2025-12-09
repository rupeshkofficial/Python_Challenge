# Ask a number from user and print the multiplication table of that number

a = int(input("Enter a number: "))
i = 1
product = 1
while i <= 10:
    product = a * i
    print(f"{a} X {i}=",product)
    i = i + 1
