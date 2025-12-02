"""
Make a list and then ask a number from user. if number exist in that list then print the position of the element else print -1
"""

my_list = [23, 5, 6,34,6,5,1]
num = int(input("Enter any number: "))

if num in my_list:
    print(my_list.index(num))
else:
    print(-1)