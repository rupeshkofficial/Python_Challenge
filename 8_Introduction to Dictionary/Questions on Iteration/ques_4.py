"""
Write a python program to multiply all the items in a dictionary.
"""

marks = {"physics": 78, "english": 91, "computer": 43, "history": 19, "chemistry": 73}

# ---- Method 1

product = 1
for v in marks.values():
    product = product * v
print(product)  # 423331818

