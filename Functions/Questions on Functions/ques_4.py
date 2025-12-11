"""
Write a function that takes an integer and prints whether it is a prime number.
"""

def is_prime(num):
    factors = 0
    for i in range(1,num+1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        print("It is a prime number")
    else:
        print("It is not a prime number")
is_prime(3)
is_prime(6)