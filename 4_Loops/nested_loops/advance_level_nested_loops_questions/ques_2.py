"""
Actual design to print
        1
      1 2
    1 2 3
  1 2 3 4  
1 2 3 4 5

Rough sketch to design
@ @ @ @ 1
@ @ @ 1 2
@ @ 1 2 3
@ 1 2 3 4
1 2 3 4 5 
"""

"""
for i in range(1,6):
    for j in range(i,5):
        print("@", end = " ")
    print()

=== O/P ===

@ @ @ @ 
@ @ @ 
@ @ 
@ 

"""

for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")

    for k in range(1, i + 1):
        print(k, end=" ")
    print()
