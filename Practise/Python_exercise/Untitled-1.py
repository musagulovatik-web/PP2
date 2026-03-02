class bank:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def deposit(self, money):
        self.balance=self.balance+money
    def withdraw(self, money):
        self.balance=self.balance-money
    def ShowBalance(self):
        print("Balance", self.balance)
class Save(bank):
    def __init__(self, balance, year, procent):
        super().__init__(balance)
        self.year=year
        self.procent=procent
    def Saves(self):
        self.balance=self.balance+(self.balance*(self.procent/100)*self.year)
        print(self.balance)
Atik=bank("Atik", 0)
Atik.deposit(1000)
Atik.withdraw(300)
Atik.ShowBalance()
Atik=Save(1000, 10, 5)
Atik.Saves()