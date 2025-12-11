# 1
def even_number():
    for i in range(1,11):
        if i % 2 == 0:
            print(i,end = " ")
even_number()

# 2
def add():
    num1 = 67 # Local Variable
    num2 = 44 # Local Variable
    print(f"Sum = {num1+num2}")

num1 = 100
num2 = 100
add ()
print(num1)
print(num2)

'''
OUTPUT:
Sum = 111
100
100

'''

# Local Varibale --> Jo variable ek fn ke under bante hai o varibale sirf usi fn ke under valid honge.


# 3

def add():
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    print(f"Sum = {num1+num2}")

def sub():
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    print(f"Sub = {num1-num2}")

add ()
sub()


