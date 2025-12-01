# Make your own list and print the sum of all even numbers present in that list

my_list = [51, 85, 1748,52,44,100, 200]
total = 0

# Iterate by Value
# for i in my_list:
#     if i % 2 == 0:
#         total = total + i
# print(total)




# Iterate by Index
for i in range(0,len(my_list)):
    if my_list[i] % 2 == 0:
        total = total + my_list[i]
print(total)