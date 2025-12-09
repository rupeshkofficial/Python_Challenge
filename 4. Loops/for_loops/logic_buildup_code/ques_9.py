# Ask a number from user and print the multiplication table of that number.

num = int(input("Enetr any number: "))
product = 1
for i in range(1,11):
    product = num * i
    print(f"{num} * {i} =",product)
