'''
Takes a charcter as input and prints whether it's vowel or a constant. ( Multiple OR will be used.)


'''

char = input("Enter any character: ")

if char == 'A' or char == 'a' or char ==  'E' or char ==  'e' or char ==   'I' or char ==  'i' or char ==  'O' or char ==  'o' or char ==  'U' or char ==  'u':
    print(f"{char} is vowel")
else:
    print(f"{char} is constant")