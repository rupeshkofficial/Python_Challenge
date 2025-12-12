"""
1. *args called Arguments --> It is a tuples || Jb hm nhi pata ki kitne arguments honge then use args
2. **kwargs called keyword Arguments --> It is a dictionary || agr named parameters ho tb kwargs use kro

Example:

def add(*args,**kwargs):
    print(kwargs)
add(name = "Raja",age = 10, gender = "male")

Output: --> {'name': 'Raja', 'age': 10, 'gender': 'male'}


"""


# 1
def add(*args, **kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)
add(name="Raja", age=10, gender="male")

# 2
# Here: n1,n2 kr baad jitne sara parameters honge o args me jayenge.

def add(n1,n2,*args, **kwargs):
    print(f"{n1 = }") # n1 = 10
    print(f"{n2 = }") # n2 = 15 
    print(f"{args = }") #  args = (20, 200, 34, 5, 6)
    print(f"{kwargs = }") # kwargs = {'name': 'Raja'}

add(10,15,20,200,34,5,6, name = "Raja")
 



