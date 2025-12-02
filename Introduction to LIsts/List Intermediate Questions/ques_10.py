"""
Write a code to split the given list into two halves.
"""

my_list = [12, 34, 56, 23, 46, 78, 45, 2, 45]

mid = len(my_list) // 2
first_half = []
second_half = []

for i in range(len(my_list)):
    if i < mid:
        first_half.append(my_list[i])
    else:
        second_half.append(my_list[i])

print("First half:", first_half)
print("Second half:", second_half)

