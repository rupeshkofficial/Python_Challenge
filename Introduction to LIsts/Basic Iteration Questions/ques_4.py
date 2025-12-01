# make your own list and print all the elements present at even index position.

my_list = [ 5, "Rupesh", 85, 91, 55.4, 100, 200]

# Iterate by Index
for i in range(0,len(my_list)):
    if i % 2 == 0:
        #print(i, end = " ") #Even Position Print 

        print(my_list[i], end = " ")