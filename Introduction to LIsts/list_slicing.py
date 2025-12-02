"""
-----------------------------------   LIST SLICING --------------------
Ex: 
      -8  -7  -6  -5 -4   -3  -2   -1
a = [ 34, 21, 67, 54, 11, 78, 90, 100]
      0   1   2   3   4   5   6    7
     

b = a[0:4] --> Output: 34,21,67,54
b = a[0:8:2] --> Output: 34,54,90 (From 0 to 8 by skipping 2 steps)
b = a[3:6] --> Output---> 54,11,78
b = a[-4:-1] --> Output --> 11,78,90
b = a[2:] (Start from 2 to end) Output--> 67,54,11,78,90,100 ---> Step +ve then move form left to Right
b = a[4:1:-1] Output--> 11, 54, 67 --------> Step -ve then move form Right to left
b = a[:4] Output --> 34, 21, 67, 54 ( Start from 0 to 4th position. here step is by default +ve)
b = [:] (Nothing given here so we have to take 1 step +ve) Output -->  34, 21, 67, 54, 11, 78, 90, 100]
b = [7:3:-1] Output --> 100,90,78,11
b = [::-1] --> Reverse (from Right to left)
a = [:len(a)//2]
"""

a = [ 34, 21, 67, 54, 11, 78, 90, 100]
b = a[::-1] #O/P: [100, 90, 78, 11, 54, 67, 21, 34]
print(b)