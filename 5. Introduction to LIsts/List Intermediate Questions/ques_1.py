"""
Make a list of your own and remove the duplicates elements from that list.
"""

my_list = ["Raja","Ravi",23, 5, 6,34,6,"Raja",5,1]
result = []
for i in my_list:
    if i not in result:
        result.append(i)
print(result)