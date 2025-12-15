#---------- 1.
# a = 15

# def change():
#     a = 30 # Local Variable
#     print(a)

# print(a) # 15
# change(a) # 30
# print(a) # 15

# ----------------

b = 15

def change():
    global b
    b = 30
    print(b)

print(b) # 15
change() # 30
print(b) # 30