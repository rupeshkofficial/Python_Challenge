# Take a argument which will be a number and make a list 0 to N

make_list = lambda n: [i for i in range(0, n + 1)]

length = int(input("Enter length = "))
list1 = make_list(length)
list2 = make_list(15)

print(f"{list1 = }") # list1 = [0, 1, 2, 3, 4, 5]
print(f"{list2 = }") # list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
