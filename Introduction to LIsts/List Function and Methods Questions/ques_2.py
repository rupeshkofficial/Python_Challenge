'''
Create a list and prompt the user for an old number followed by a
new number. If the old number exists in the list replace the new number
provided by the user.

'''

my_list = [56,78,78,5,8,4,5,7,3,34]
old_number = int(input("Enter old number: "))
new_number = int(input("Enter new number: "))

for i in range(0,len(my_list)):
    if my_list[i] == old_number:
        my_list[i] = new_number
print(my_list)
