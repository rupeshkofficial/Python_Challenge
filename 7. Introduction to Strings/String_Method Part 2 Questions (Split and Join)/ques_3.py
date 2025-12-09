"""
Write a program that reverse each word in a sentence while maintaining the word order.

Example: "Hello World" ----> Output : "olleH dlroW"

"""
my_string = "Python is GOod"
words = my_string.split() # ['Python', 'is', 'Good'] --> String in list

result = " ".join(i[::-1] for i in words)
print(result) # nohtyP si doOG