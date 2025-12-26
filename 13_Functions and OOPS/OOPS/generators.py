# Yield

def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# for i in numbers():
#     print(i)

x = numbers()
print(next(x)) # next ka kaam hai pahli value lekar aana
print(next(x))


# for i in range(1,11):
#     print(i)

