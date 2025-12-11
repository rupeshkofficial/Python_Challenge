a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8, 9]

c = set(a)
d = set(b)

#print(c.intersection(d)) # {4, 5}

result =list (c.intersection(d))
print(result) # [4, 5]

