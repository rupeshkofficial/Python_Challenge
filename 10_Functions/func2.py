# ------------- Parameters & Arguments ------------


def add(a, b):  # a, b --> Parameters
    print(a + b)


add(9, 23)  # 9, 23 --> Arguments
add(100,200)
add("Python","Language")

x = int(input("Enetr number 1 = "))
y = int(input("Enetr number 2 = "))
add(x,y)

#add()                #  TypeError: add() missing 2 required positional arguments: 'a' and 'b'
#add (2)             #  TypeError: add() missing 1 required positional argument: 'b'
#add (2,4,7)        #  TypeError: add() takes 2 positional arguments but 3 were given
#add("Python",12)   # TypeError: can only concatenate str (not "int") to str
