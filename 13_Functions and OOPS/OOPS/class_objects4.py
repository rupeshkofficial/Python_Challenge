class Student:
    def __init__(self) -> None:
        self.name = input("Enter name = ")
        self.age = int(input("Enter age = "))
        
    def display_inf(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")

    def change_name(self,new_name: str):
        self.name = new_name

s1 = Student()
s1.display_inf()
s1.change_name("XYZ")
s1.display_inf()