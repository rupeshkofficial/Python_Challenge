# Make your own list and print how many Positive and negative numbers are in list

my_list = [2,4,5,7,-2,4,6,-9,-56]
positive_num = 0
negative_num = 0

for i in my_list:
    if i > 0 :
        positive_num = positive_num + 1
    else:
        negative_num = negative_num + 1
print(f"Positive number = {positive_num} and Negative number = {negative_num}")
        