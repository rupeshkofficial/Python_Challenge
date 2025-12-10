"""
Write a python program to check if two given sets have no elements in common.
"""

set1 = {5,6,2,1,"Rupesh",7}
set2 = {"Python",76,22,91,-991,7}

result = set1.intersection(set2)
print(result) 
print(len(result))

if len(result) == 0:
    print("Both ets have nothing in common")
else:
    print("Sets have something in common")
    print(result)