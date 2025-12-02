"""
Write a program that hjas two list and make a new list that contains only the common
elements between them without duplicates.
"""
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
result = []

for i in list1:
    if i in list2:
        if i not in result:
            result.append(i)
print(result)