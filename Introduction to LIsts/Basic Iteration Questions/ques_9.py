# Make your own list and find the sum of all numbers divisible by 3 or 4.

my_list = [51, 85, 1748,52,44,100, 200]
total = 0

# Iterate by Value
# for i in my_list:
#     if i % 3 == 0 or i % 4 == 0:
#         total = total + i
# print(total)



# Iterate by Index\
for i in range(0,len(my_list)):
    if my_list[i] % 3 == 0 or my_list[i] % 4 == 0:
        total = total + my_list[i]
print(total)