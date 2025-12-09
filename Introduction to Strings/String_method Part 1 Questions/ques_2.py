"""
Ask a string from user and count the number of UpperCase and LowerCase character in that string.
"""

# --------------------------- Method 1

 
my_string = "RuSdfpesh1234#67&"

upper_case_count = 0
lower_case_count = 0

for ch in my_string:
    if ch.isupper():
        upper_case_count += 1
    elif ch.islower():
        lower_case_count += 1
print(upper_case_count) # O/P : 2
print(lower_case_count) # O/P : 7


# ---------------------------- Method 2

my_string = "RuSdfpesh1234#67&"

upper_case_count = 0
lower_case_count = 0

