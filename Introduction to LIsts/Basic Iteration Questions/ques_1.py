# Make your own list and print the list in reverse

'''
a = [23,46,"Raja",4,56,24]
for i in range(len(a),0,-1):
    print(a[i-1],end = " ")

'''

my_list = [3,4,6,"Rupesh",100,21,34]

# Position --> 0 to 5
# Reverse --> 5 to 0
# length = 6

for i in range(len(my_list)-1,-1,-1):
    print(my_list[i],end = " ")
