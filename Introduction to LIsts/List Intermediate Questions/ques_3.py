"""
Take 10 integer input from the user and store them in a list. Now, Copy all the elements in another list but 
in reverse order.
"""

print("Enter 10 numbers! ")
my_list = []
another_list = []

for i in range(0,11):
    num = int(input(f"Enter number at Index {i}= "))
    my_list.append(num)

print(my_list)


for i in range(len(my_list)-1, -1, -1):
    another_list.append(my_list[i])
print(another_list)