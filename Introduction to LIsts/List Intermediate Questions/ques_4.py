"""
Write a program to find the average of all the numbers present in the list.
"""

my_list = [34,45,56,24,24,-34]
total = 0
for i in my_list:
    total = total + i
    average = total/len(my_list)
print(average)