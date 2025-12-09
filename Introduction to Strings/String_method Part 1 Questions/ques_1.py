"""
Ask a string from user and count how many alpahbets are there in that string.
"""

# --------------------------- Method 1

# my_string = "Rupesh1234#67&"

# count = 0

# for ch in my_string:
#     if ch.isalpha():
#         count = count + 1
# print(count) # O/P : 6


# -------------------------------------- Method 2
# Method 2 ( Using Ascii code)
# Ascii of A - Z ==> 65 - 90
# Ascii of a - z ==> 97 - 122

my_string = "Rupesh1234#67&"
count = 0
for ch in my_string:
    ascii = ord(ch)
    if (ascii > 60 and ascii < 90) or (ascii > 97 and ascii < 122):
        count = count + 1

print(count) #  O/P : 6
