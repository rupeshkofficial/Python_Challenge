"""
Write a code that swaps the first and last elements of a given list.
"""

my_list = [32, 10, "Rupesh", 55.90, "xyz"]

temp = my_list[0]        # store first element
my_list[0] = my_list[-1] # move last to first
my_list[-1] = temp       # assign stored first to last

print(my_list)

