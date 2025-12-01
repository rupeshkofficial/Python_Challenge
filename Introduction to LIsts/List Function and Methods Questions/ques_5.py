'''
Generate a list of atleas 10 numbers. Then, create two seperate list called "odd" and "even".
Put all the odd numbers from the original list into the "odd" list and even numbers into "even" list

'''

my_list = [1,25,65,46,99,3,4,5]
even = []
odd = []

# Iterate by Index
# for i in range(0,len(my_list)):
#     if my_list[i]%2 == 0:
#         even.append(my_list[i])
#     else:
#         odd.append(my_list[i])
# print(even)
# print(odd)



# Iterate by Value
for num in my_list:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(f"Even List = {even}")
print(f"Odd List = {odd}")