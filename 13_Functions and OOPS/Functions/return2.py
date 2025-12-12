def add(n1,n2):
    total = n1 + n2
    return total

def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

x = int(input("Enter number 1 = "))
y = int(input("Enter number 2 = "))

s = add(x,y)
print(check(s))