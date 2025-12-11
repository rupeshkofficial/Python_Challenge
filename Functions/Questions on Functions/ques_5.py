"""
Write a function that takes a list of numbers and prints the sum and avergae of these numbers.
"""

def sum_avg_list(lst):
    total = 0
    for num in lst:
        total = total + num   
    print(f"Total of all numbers = {total}")
    avg = total / len(lst)
    print(f"Avg of all numbers = {avg}")
sum_avg_list([2,3,5,6,3,5])
sum_avg_list([59,74,-85,100,63])
