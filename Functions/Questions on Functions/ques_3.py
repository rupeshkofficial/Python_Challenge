"""
Write a function that takes three numbers as parameters and print the largest among them.  Three numbers is different    
"""

# def largest_numbers(a,b,c):
#     if a > b and a > c:
#         print("1st --> a is Largest")
#     elif b > a and b > c:
#         print("2nd --> b is Largest")
#     else:
#         print("3rd --> c is Largest")
# largest_numbers(34,45,2)


# ---------------        JUST FOR LOGIC CHECK

def largest_numbers(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print(num1)
        print(f"{num1} is the largest")
    elif num2 > num1 and num2 > num3:
        print(num2)
        print(f"{num2} is the largest")
    else:
        print(num3)
        print(f"{num3} is the largest")
largest_numbers(10,10,10)