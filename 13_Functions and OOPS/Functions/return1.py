def addition(num1, num2):
    total = num1 + num2
    return total

# Jo chiz return krta hai use hm kisi varibale me save krte hai aur print krte hai.
x = addition(3, 4)  
print(x)  

# Jo chiz return krta hai use hm directly print v kr sakte hai.
print(addition(3, 4) )


#-------------------------------- Agr fn kuch v return nhi krta hai aur phir v hm use kisi variable me save krke print krte hai to by default NONE print krega ------------

def addition(num1, num2):
    total = num1 + num2
    print(total) # 59
x = addition(3,56)  # Yha hme fn ke through kuch v return nhi aa rha hai to x me None hoga aur None hi print hoga for x.
print(x) # None