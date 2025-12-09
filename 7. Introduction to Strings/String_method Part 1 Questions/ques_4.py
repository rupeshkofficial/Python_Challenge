"""
Ask a string from user and convert all the alphabets to LowerCase
"""

# ------------------------- Method 1

my_string = "RajaRupesw3e3$#hji"

result = my_string.lower()
print(result) # O/P : rajarupesw3e3$#hji


# -------------------------- Method 2 ( Using Ascii )

'''
ASCII of ( A - Z ) : 65 - 90
ASCII of ( a - z ) : 97 - 122

Now, if we want to convert A to a then we can add ascii of A + 32 that will be 65 + 32 = 97 and 97 is the ascii value of a. When we need in uppercase then we will substract -32

Why add 32--> Because the the difference of  ascii value of a and A is  ( 97 - 65) = 32.

'''

my_string = "abASDc123#%)(*)Ab2e"
result = ""

for ch in my_string:
    ascii = ord(ch)

    if ascii >= 65 and ascii <= 97 :
        new_ascii = ascii + 32
        char = chr(new_ascii)
        result += char
    else:
        result += ch

print(result) # O/P : basdc123#%)(*)ab2e



