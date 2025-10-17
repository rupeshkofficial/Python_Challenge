'''
Takes integer input and prints whether it's positive, negative (Consider 0 as positive)
'''


num = float(input("Enter any number: "))

if num >= 0:
    print(f"{num} is positive!")
else:
    print(f"{num} is negative")