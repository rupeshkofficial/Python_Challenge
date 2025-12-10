'''
Ask the user for a number. Then, from a list of numbers, remove akk the numbers that can be divided by the numbers from the user entered.
'''

my_list = [10,15,20,25,30]
new_list = []
num = int(input("Enter any number: "))
for i in my_list:
    if i%num != 0:
        new_list.append(i)
print(new_list)
