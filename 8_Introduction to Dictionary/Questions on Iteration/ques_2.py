"""
Convert two list into a dictionary. Make two list on your own of same lenght and convert them to dictionary.
"""

list1 = ["Python", "good", "done", "bye"]
list2 = [54, " wow", "Rupesh", 99]
result = {}

for i in range(0,len(list1)):
    result[list1[i]] = list2[i]
    
print(result) # {'Python': 54, 'good': ' wow', 'done': 'Rupesh', 'bye': 99}