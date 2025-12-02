"""
Write a code to find the occurance of each element in a list and print the element with highest occurance.
"""

my_list = [5,1,"Code and debug",56.32,5,"Rupesh",1,3,4,5,6]
result = []

for num in my_list:
    if num not in result:
        result.append(num)

highest_occ_element = 0
highest_occurance = 0

for num in result:
    c = my_list.count(num)
    print(f"Occurance of {num} is = {c} times")

    if c > highest_occurance:
        highest_occurance = c
        highest_occ_element = num

print(f"Highest Occurancer Element is {highest_occ_element}")