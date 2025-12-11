"""
Ask a string from user, remove all the duplicates from that string and print thta string again (Order doesn't matter)
"""

my_string = "dfrtgfnbtrgjrefsdhdbverjknxcverfbh"

result = set(my_string)
print(result)

joined_string = "".join(result)
print(joined_string)