"""
Coun the number of spaces in a string entered by user
"""

# ------------------------ Method 1
my_string = " Ra wdesfdew )_ wd dcf ed d ee1221"

count = 0

for ch in my_string:
    if ch == " ":
        count = count + 1
print(count) # O/P : 8


# ------------------------ Method 2
# Ascii code of space is 32

my_string = " Ra wdesfdew )_ wd dcf ed d ee1221"

count = 0

for ch in my_string:
    if ord(ch) == 32:
        count = count + 1
print(count) # O/P : 8

