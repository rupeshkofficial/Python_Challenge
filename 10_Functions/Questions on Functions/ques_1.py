"""
Write a function that accepts an integer and prints the 
multiplication table for that number upto 10.

5

5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
...
5 * 10 = 50
"""

def multiplication_table(num):
    for i in range(1,11):
        print(f"{num} X {i} = {num * i}")
multiplication_table(10)
multiplication_table(3)