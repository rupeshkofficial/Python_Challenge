my_set = {1,2,3,4,5,6,7,8}
num = int(input("Enter a number = "))

# ----- Method 1

# found = False
# for i in my_set:
#     if i == num:
#         found = True
# if found:
#     print("Yes")
# else:
#     print("No")


# ---- Method2 using membership operator

if num in my_set:
    print("Yes")
else:
    print("No")