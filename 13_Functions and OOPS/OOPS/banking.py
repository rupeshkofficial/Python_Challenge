from random import randint


class Bank:
    def __init__(self) -> None:
        self.account = randint(10000, 999999)
        self.full_name = input("Enter name = ")
        self.phone_number = int(input("Enter Phone Number = "))
        self.balance = 0

    def show_info(self):
        print(f"Account Number = {self.account}")
        print(f"Full Name = {self.full_name}")
        print(f"Balance = {self.balance}\n")

    def show_balance(self) -> None:
        print(f"Current Balance = {self.balance}")

    def withdraw(self) -> None:
        amount = int(input("Enter amount to withdraw = "))
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            # self.balance = self.balance - amount
            self.balance -= amount

    def deposit(self) -> None:
        amount = int(input("Enter amount to deposit = "))
        self.balance = self.balance + amount


# ----------------------         --------------------
# b1 = Bank()
# b1.show_balance()

# b1.deposit()
# b1.show_balance()

# b1.withdraw()
# b1.show_balance()

# ------------ List of Object ---------

# banks = []
# x = Bank()
# banks.append(x)
# print(banks)

# y = Bank()
# banks.append(y)
# print(banks)

# banks[0].show_balance()
# banks[1].deposit()
# banks[1].show_balance()

# --------------- Used while loops to overcome from List of objects ----------


banks = []

def check_account_exists(acc_no: int):
    global banks
    for obj in banks:
        if obj.account == acc_no:
            return obj
    return None



while True:
    print("1. Create Account")
    print("2. Show All Bank Details")
    print("3. Deposit amount")
    print("4. Withdraw amount")
    print("5. Transfer amount")
    print("6. Exit")
    choice = int(input("Enter choice = "))
    if choice == 1:
        obj = Bank()
        banks.append(obj)
        print(banks)
    elif choice == 2:
        if len(banks) == 0:
            print("No accounts have been created yet")
        else:
            for account in banks:
                account.show_info()
    elif choice == 3:
        if len(banks) == 0:
            print("No accounts have been created yet")
        else:
            acc_no = int(input("Enter account number to deposit = "))
            for obj in banks:
                if obj.account == acc_no:
                    obj.deposit()
                    break
    elif choice == 4: 
        if len(banks) == 0:
            print("No accounts have been created yet")
        else:
            acc_no = int(input("Enter account number to withdraw = "))
            for obj in banks:
                if obj.account == acc_no:
                    obj.withdraw()
                    break
    elif choice == 5:
        from_acc_no = int(input("Enter account number from which you want to transfer = "))
        to_acc_no = int(input("Enter account number to which you want to transfer = "))
        
        to_acc_no = int(input("Enter account number to which you want to transfer = "))
        from_acc_obj = check_account_exists(from_acc_no) 
        to_acc_obj = check_account_exists(to_acc_no)
        if from_acc_obj != None and to_acc_no != None:
            transfer_amount = int(input("Enter transfer amount = "))
            if from_acc_obj.balance < transfer_amount:
                print("Insufficient balance")
            else:
                from_acc_obj.balance -= transfer_amount
                to_acc_obj.balance += transfer_amount
            
        else:
            print("Account does not exists")



    elif choice == 6:
        break
    else:
        print("Invalid Choice")