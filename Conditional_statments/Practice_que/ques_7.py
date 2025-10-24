"""
Ask Number from user:

Print "Fizz" if the number is divisible by 3
Print "Buzz" if the number is divisible by 5
Print "FizzBuzz" if the number is divisible by 3 and 5 are true
print the number itself if none of the condition

"""

num = int(input("Enter any Number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0 :
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")