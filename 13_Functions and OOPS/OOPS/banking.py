from random import randint


class Bank:
    def __init__(self) -> None:
        self.account = randint(10000, 999999)
        self.full_name = input("Enter name = ")
        self.phone_number = int(input("Enter Phone Number = "))
        self.balance = 0

    def show_balance(self) -> None:
        print(f"Current Balance = {self.balance}")

    def withdraw(self) -> None:
        amount = int(input("Enetr amount to withdraw = "))
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            # self.balance = self.balance - amount
            self.balance -= amount

    def deposit(self) -> None:
        amount = int(input("Enter amount to deposit = "))
        self.balance = self.balance + amount

b1 = Bank()
b1.show_balance()

b1.deposit()
b1.show_balance()

b1.withdraw()
b1.show_balance()