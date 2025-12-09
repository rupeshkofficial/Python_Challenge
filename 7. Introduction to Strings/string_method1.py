a = "rupesh kumar company name 3#45 () %$ ruPEsh tech 234"
x = a.title() # First letter of each word will be became Capital and rest will be small letter. If any word have all capital then they will change all letter to small except 1st letter
print(x) # Rupesh Kumar Company Name Rupesh Tech

x = a.capitalize() # 1st letter of sentence will be capital and rest will be small
print(x) # Rupesh kumar company name rupesh tech 234

x = a.upper() # All letter will be in upper case
print(x) # RUPESH KUMAR COMPANY NAME RUPESH TECH 234

x = a.lower() # All letter will be in lower case
print(x) # rupesh kumar company name rupesh tech 234

x = a.swapcase() # Small letter swapped with capital letter and Capital letter swapped with small letter
print(x) # RUPESH KUMAR COMPANY NAME RUpeSH TECH 234


x = a.isupper()
print(x) # False

y = "RUPESH4535%$"
z = y.isupper()
t = y.islower()
print(z) # True
print(t) # False


r= "Rajaded12"
s = r.isalpha() # To check string contain all alphabets
print(s) # False

s = r.isalnum() # Only it should only alphabets and number
print(s) # True

c = "Rajdweewed123f"
d = c.isdigit() # All should digits
print(d) # False

e = "72348234"
f = e.isdigit()
print(f) # True

g = "\n\t     "
h = g.isspace()
print(h) # True



#------------------------------------------------

a = "Rupesh123"

if a.isdigit():
    a = int(a)
    print(a,type(a))
else:
    print('Cannot be converted to integer')