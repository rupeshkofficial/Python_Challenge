"""
Write a program that prompts the user to specify the length of a list and then request numbers to populate
that list. Display the final list as the output.

"""

list_length = int(input("Enter the length of the list: "))
result = []
for i in range(0, list_length):
    # num = int(input("Enter number: "))
    num = int(input(f"Enter number at position {i}: "))
    result.append(num)
print(result)
