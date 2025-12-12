def add(x: int, y: int) -> int:
    total = x + y
    return total


def greet(name: str, age: int, percentage=float) -> None:
    print(name)
    print(age)
    print(percentage)


c = add(2, 4)
print(c)
greet()
