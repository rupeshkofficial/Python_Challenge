"""
Given two lists a,b. Check if two list have atlest one element common in them.
"""

list1 = [ 3,6,7,5,55,3,1,2,2,"Python", "Rupesh"]
list2 = [7,8,5,6,1,"Rupesh"]

#set1 = set(list1)
#set2 = set(list2)

#print(set1.intersection(set2)) # {1, 5, 6, 7, 'Rupesh'}

# Here:  & --> intersection , | -->  Union
#print(set1 & set2) # {1, 5, 6, 7, 'Rupesh'}

print(set(list1) & set(list2)) # {1, 5, 'Rupesh', 6, 7}