# Make your own list and print all the odd numbers present in the list

my_list = [51, 74, 85, 91, 52, 44]

# Iteration by Value
# for i in my_list:
#     if i % 2 != 0:
#         print(i, end = " ")



# Iteration by Index
for i in range(0,len(my_list)):
    if my_list[i] % 2 != 0:
        print(my_list[i], end = " ")
    
    
    
    