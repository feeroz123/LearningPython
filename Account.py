class Account:

    def __init__(self, owner_name, initial_balance=0.0):
        self.owner = owner_name
        self.balance = initial_balance

    def __str__(self):
        return "Account owner = " + self.owner + "\n" + f"Account Balance = {self.balance}"

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited in account:", amount)

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
            print("Amount withdrawn from account:", amount)

    def get_balance(self):
        print("Account Balance = {}".format(self.balance))


print("Welcome to our Bank ! Please enter initial details for the account.")
name = input("Enter your name: ")
balance = float(input("Enter initial balance: "))

owner_account = Account(name, balance)
print(owner_account)    # Calling the __str__ function when the object is used in 'print'


owner_account.deposit(100)
owner_account.deposit(200)
owner_account.withdraw(300)
owner_account.withdraw(400)

owner_account.get_balance()
