# Calculate the factorial of a number entered by user.

n = int(input("Enter any number: "))
factorial = 1

for i in range(1,n+1):
    factorial = factorial * i
print(f"Factorial of a number {n} is",factorial)