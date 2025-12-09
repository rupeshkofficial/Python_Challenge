'''
Ask physics and chemistry marks from the user
print PASS, if student is passed in both subjects
ELSE print FAIL
'''

phy = int(input("Enter Physics Marks: "))
chem = int(input("Enter Chemistry Marks: "))

if phy >= 33 and chem >= 33 :
    print("PASS")
else:
    print("FAIL")
print("Result Shown!")