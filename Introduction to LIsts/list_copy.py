a = [59, 68, 100, 5, "Anirudh", True, 55.556, "Code"]
b = a
print(a) # O/P: [59, 68, 100, 5, "Anirudh", True, 55.556, "Code"]
print(b) # O/P: [59, 68, 100, 5, "Anirudh", True, 55.556, "Code"]


# Issue: I have changed the elements of 2nd position in list a to 0. But changes done in both. Why ???? Beacuse both reference to the same address. So, Copy Came into picture now.
a[2] = 0
print(a) # O/P: [59, 68, 0, 5, 'Anirudh', True, 55.556, 'Code']
print(id(a))
print(b) # O/P: [59, 68, 0, 5, 'Anirudh', True, 55.556, 'Code']
print(id(b))


# Copy ( Refers differnt address for both a and b)
r = [59, 68, 100, 5, "Anirudh", True, 55.556, "Code"]
s = r.copy()
print(r)
print(id(r))
print(s)
print(id(s))

r[2] = 0
print(r)
print(s)