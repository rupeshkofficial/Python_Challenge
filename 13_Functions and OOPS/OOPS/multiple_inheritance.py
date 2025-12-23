class Father:
    father_name = ""

    def displayFatherName(self):
        print(self.father_name)

class Mother:
    mother_name = ""

    def displayMotherName(self):
        print(self.mother_name)

class Child(Father,Mother):
    child_name = ""

    def displayChildName(self):
        print(self.child_name)

c1 = Child()
c1.father_name = "Sanjay"
c1.mother_name = "Nisha"
c1.child_name = "Nishant"
c1.displayFatherName()
c1.displayMotherName()
c1.displayChildName()

