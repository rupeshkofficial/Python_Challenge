class Student:
    # Attributes, Class Variables ---> Variables inside class
    roll_no = 0
    name = ""
    age = 0
    gender = ""
    address = ""
    
    # We can also define fn or methods inside the class like this
    # To write self is required. As it indicates that info is the part of Student Class.
    def info(self):
        print(f"Name = {self.name}")
        print(f"age = {self.age}")
        print(f"gender = {self.gender}")



s1 = Student()
s2 = Student()
print(s1) # <__main__.Student object at 0x107b93040> --> (It is the address of object and a object that can't be print)

print(s1.roll_no) # 0
print(s1.name) # nothing print as name is blank

s1.name = "Rupesh"
s1.roll_no = 10
s1.age = 100
s1.gender = "Male"
print(s1.roll_no) # 10
print(s1.name)    # Rupesh
 
print("--------------------")
print(s2.roll_no) # 0
print(s2.name)    # nothing print as name is blank


print("-------------------------------")
s1.info()
# -------------Output---------:
# Name = Rupesh
# age = 100
# gender = Male

s2.info()

# --------- Output ------------:
# Name = 
# age = 0
# gender = 
