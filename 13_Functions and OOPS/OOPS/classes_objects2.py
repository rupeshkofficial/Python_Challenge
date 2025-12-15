class Student:
    roll_no = 0
    name = ""
    age = 0
    gender = ""
    address = ""
    
    # Methods
    def info(self):
        print(f"Name = {self.name}")
        print(f"age = {self.age}")
        print(f"gender = {self.gender}")
    
    def set_info(self):
        self.name = input("Enter Your Name = ")
        self.age = int(input("Enter Your Age = "))
        self.gender = input("Enter Your Gender = ")
        self.roll_no = int(input("Enter Your Roll_no = "))

s1 = Student()
s2 = Student()

s1.set_info()
s2.set_info()

print("---------------------")
s1.info()
s2.info()




