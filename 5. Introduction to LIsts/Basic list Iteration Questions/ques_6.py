# Make your own list and count the no of even numbers present in the list.

my_list = [51, 85, 91.66, 52, 44, 100, 200]
count = 0

# Iterate by Value
# for i in my_list:
#     if i % 2 == 0:
#         count = count + 1
# print(count)


# Iterate by Index
for i in range(0,len(my_list)):
    if my_list[i] % 2 == 0:
        count = count + 1
print(count)
