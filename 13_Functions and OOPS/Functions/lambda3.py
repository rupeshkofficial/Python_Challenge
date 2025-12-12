# Even return True else False

# Example 1 
check_even =lambda num: num%2 == 0

if check_even(151):
    print("Even")
else:
    print("Odd")


# Example 2 
check_even = lambda num : print("Even") if num % 2 == 0 else print("Odd")

check_even(100)
check_even(55)