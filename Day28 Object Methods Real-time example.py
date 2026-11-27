class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def display(self):
        print("Account Holder name : ",self.name)
        print("Balance : ",self.balance)
    def deposite(self):
        self.balance = self.balance+1000
        print("After deposite : ",self.balance)
    def withdraw(self):
        self.balance = self.balance -500
        print("After withdraw : ",self.balance)
s = BankAccount("Harini",5000)
s.display()
s.deposite()
s.withdraw()

        
