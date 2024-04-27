import random 

class BankAccount:
    def __init__(self, name, cnic, dbo):
        self.name = name
        self.cnic = cnic
        self.dbo = dbo
        self.balance =  0
        self.accountNumber = random.randint(1000, 10000)

    def deposit_amount(self, amount):
        self.balance = self.balance + amount

    def withdraw_amount(self, amount):
        if self.balance > 0:
            self.balance = self.balance - amount

    def account_details(self):
        print("="*50)
        print(f"Name:           {self.name}")
        print(f"Account Number: {self.accountNumber}")
        print(f"Cnic:           {self.cnic}")
        print(f"Date of Birth:  {self.dbo}")
        print(f"Balance:        {self.balance}")
        print("="*50)



ibad = BankAccount("Ibad", "16201-2390477-3", "11-May-2002")
gulalam = BankAccount("Gulalam", "16201-3216578-9", "07-May-2000")

ibad.deposit_amount(1000)
ibad.account_details()

gulalam.deposit_amount(100)
gulalam.account_details()