"""
Write a python program to sum all the items in a dictionary.
"""

marks = {"physics": 78, "english": 91, "computer": 43, "history": 19, "chemistry": 73}

# ---- Method 1

total = 0
for v in marks.values():
    total = total + v
print(total)  # 304

# ---- Method 2

print(sum(list(marks.values()))) # 304

# ---- Method 3