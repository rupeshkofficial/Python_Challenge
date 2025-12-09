"""
Count
Startswith
Endswith
Index
Find
Replace
Strip --> Remove white space from left side as well as righ side
"""

my_string = "hello world"

c = my_string.count("e")
print(c) # 1


c = my_string.startswith("e")
print(c) # False

c = my_string.endswith("d")
print(c) # True

c = my_string.index("d")
print(c) # 10

# c = my_string.index("z")
# print(c) # ValueError: substring not found

c = my_string.find("z")
print(c) # -1 (In case of failure, I mean if character is not in string)


c = my_string.replace("l","z")
print(c) # hezzo worzd


my_string1 = "     Hello Bhai!     "
print(my_string1) #      Hello Bhai!     --> with space without using strip

c = my_string1.strip()
print(c) # Hello Bhai! --> Without space with using strip


my_string2 = "@@@@@@@Hello Bhai!@@@@@"
print(my_string2) # @@@@@@@Hello Bhai!@@@@@    --> with @ without using strip

c = my_string2.strip("@")
print(c) # Hello Bhai! --> Without @ with using strip