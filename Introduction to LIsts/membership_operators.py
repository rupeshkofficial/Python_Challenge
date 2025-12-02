"""
------------------------  Membership Operators ---------------------
1. IN
2. NOT IN

:> To check any elements in sequence or not. Sequence are list,tuples, string, dictionary
:> Always gives boolena return. i.e TRUE / FALSE


"""

a = [59,68,100,5,"Rupesh",True,55.556,"Code"]
print("Rupesh" in a) # O/P : True
print(105 not in a) # O/P : True
print(68 not in a) # O/P : False

# Ask a number from the user and print YES if number exists in list else print NO

#---------- 1st approach
# num = int(input("Enetr any number: "))
# if num in a:
#     print("YES")
# else:
#     print("NO")


#------------ 2nd approach
num = int(input("Enetr any number: "))
if a.count(num) > 0:
    print("YES")
else:
    print("NO")
