class Student:
    def __init__(self):
        self.name = input("Enter Your Name = ")
        self.age = int(input("Enter Your Age = "))
        self.gender = input("Enter Your Gender = ")
        self.roll_no = int(input("Enter Your Roll_no = "))

    def info(self):
        print(f"Name = {self.name}")
        print(f"age = {self.age}")
        print(f"gender = {self.gender}")


s1 = Student() 
s1.info()

s2 = Student()
s2.info()
