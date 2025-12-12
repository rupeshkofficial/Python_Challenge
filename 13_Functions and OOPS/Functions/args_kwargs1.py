'''
Concept: ---> Jitne me parameters hm bhejenge. O sare ke sare args me aa jayenge as a tuple.
              We use it when we don't have idea that how many arguments there.
Example:


def add(*args):
    print(args)
add(1,2,3)
add(2,3,4,6,7,8)
add(12,34)

Output: (1, 2, 3)
        (2, 3, 4, 6, 7, 8)
        (12, 34)

'''


# We use args it when we don't have idea that how many arguments there.
# Example:

def add(*args):
    print(sum(args))
add(22,34)
add(23,4,5,67,2,5,2,43)
add(2)


# We can't add if we pass list as arguments. It will give error
#Example:

def add(*args):
    print(args)
    print(sum(args))

add([23,4354,5,32],34,2,4,[34,5,56,3],34,2) # TypeError: unsupported operand type(s) for +: 'int' and 'list'