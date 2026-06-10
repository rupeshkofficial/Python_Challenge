num = int(input("Enter any number: "))

n = num
result = 0

while n > 0:
    last_digit = n % 10
    result = (result * 10) + last_digit
    n = n // 10

if result == num:
    print("Palindrome")
else:
    print("Not Palindrome")



