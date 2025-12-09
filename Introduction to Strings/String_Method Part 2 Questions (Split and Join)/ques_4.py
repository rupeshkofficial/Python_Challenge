"""
Write a program that converts a string in Camel_Case to Snake_Case.

Ex: "helloWorldHowAreYou" ----> O/P: "hello_world_how_are_you"
"""

my_string = "helloWorldHowAreYou"
result = ""

for ch in my_string:
    if ch.isupper():
        result += "_" + ch.lower()
    else:
        result += ch

print(result)


