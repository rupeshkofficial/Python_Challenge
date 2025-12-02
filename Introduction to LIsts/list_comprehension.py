my_list = [i for i in range(1,21)]
print(my_list) #O/P: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

my_list = ["even" for i in range(1,21)]
print(my_list) #O/P: 'even', 'even', 'even', 'even', 'even', 'even', 'even', 'even', 'even', 'even', 'even', 'even', 'even', 'even', 'even', 'even', 'even', 'even', 'even', 'even']

my_list = [ i % 2 for i in range(1,21)]
print(my_list) #O/P: [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# Here: Kya add krna hai
my_list = ["EVEN" if i %2 == 0 else "ODD" for i in range(0,21)]
print(my_list) # O/P: ['EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN', 'ODD', 'EVEN']

# Here: Kab Add krna hai
# [2,4,6,8,10,...........26,28,30]
my_list = [ i for i in range(1,31) if i % 2 == 0]
print(my_list) # O/P: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]