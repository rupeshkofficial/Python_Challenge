"""
Ask a string from user. Convert UpperCase to lowerCase and Convert LowerCase to uppercase and don't chnage the others letters.
"""

my_string = "RaJaBaBUdew243%&^KUmar"

result = ""

for ch in my_string:
    ascii = ord(ch)
    if ascii >= 97 and ascii <= 122:
        new_ascii = ascii - 32
        char = chr(new_ascii)
        result += char
    elif ascii >= 65 and ascii <= 97:
        new_ascii = ascii + 32
        char = chr(new_ascii)
        result += char
    else:
        result +=ch
print(result) # O/P : rAjAbAbuDEW243%&~kuMAR