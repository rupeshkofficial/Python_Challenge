"""
Ask a string from user and print the count of how many alphabets, digits,spaces and symbols (everything else) are there in that string.
"""

my_string = "adb12@ $% 2 Ab"

alpha_count = 0
digit_count = 0
spaces_count = 0
symbols_count = 0

for ch in my_string:
    if ch.isalpha():
        alpha_count += 1
    elif ch.isdigit():
        digit_count += 1
    elif ch == " ":
        spaces_count += 1
    else:
        symbols_count += 1

print(alpha_count) # 5
print(digit_count) # 3
print(spaces_count) # 3 
print(symbols_count) # 3