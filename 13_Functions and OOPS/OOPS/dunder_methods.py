# Protected
class Father:
    def __init__(self) -> None:
        self.father_name = input("Enter father name = ")
        self._bank_balance = int(input("Enter father bank balance = ")) # Protected
        self.__phone_model = input("Enter phone model = ") # Private

    def __str__(self) -> str:
        return f"Father name = {self.father_name}\nFather bank balace = {self._bank_balance}\nFather phone model = {self.__phone_model}"

    # def displayFather(self):
    #     print(f"Father name = {self.father_name}")
    #     print(f"Father bank balace = {self._bank_balance}")
    #     print(f"Father phone model = {self.__phone_model}")

obj1= Father()
obj2 = Father()
print("-------------")
# print(obj)
# obj.displayFather()
print(obj1)
print(obj2)