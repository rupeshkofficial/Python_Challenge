"""
Write a function that takes a stringt and prints whether it is a palindrome.

noon ==> noon
mom ===> mom
"""

def check_palindrome(string):
    if string == string[::-1]:
        print("It is a Palindrome")
    else:
        print("It is not a Palindrome")

check_palindrome("moom")
check_palindrome("rupeshj")