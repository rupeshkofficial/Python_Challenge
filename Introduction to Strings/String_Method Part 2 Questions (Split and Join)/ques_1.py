# Write a program to reverse the order of words

my_string = "Python is Good"
words = my_string.split() # ['Python', 'is', 'Good'] --> String in list

words = words[::-1] # ['Good', 'is', 'Python'] # Reverse the list

result = " ".join(words) # Words is join by spaces
print(result) # Good is Python