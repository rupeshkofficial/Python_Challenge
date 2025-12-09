"""
Write a program that accepts a string and capitalizes the first letter
of each word while converting all other letters to lowercase
"""
my_string = "Python is GOod"
words = my_string.split() # ['Python', 'is', 'Good'] --> String in list

result = " ".join(i.capitalize() for i in words)
print(result) # Python Is Good