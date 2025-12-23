# Many forms

class Animal:
    def sound(self):
        print("Animal Speaking!")
    
class Dog(Animal):
    def sound(self):
        print("Bhaw Bhaw Bhaw!!!!")
class Cat(Animal):
    def sound(self):
        print("Meow Meow Meow!!!")

obj = Dog()
obj.sound()
