class BankAccount:
    def __init__(self, balance):
        self.balance=balance
    
    
    def deposit(self, a):
        self.balance += a
        print(f"Balance after deposit is : {self.balance}")
        
    def withdraw(self, a):
        if (a<=self.balance):
            self.balance -= a
            print(f"Balance after Withdrawl is : {self.balance}")
        
        else:
            print(f"Insufficient funds. current balance is: {self.balance}")
class BonusAmount(BankAccount):
    def __init__(self, balance,bonus):
        super().__init__(balance)
        self.bonus=bonus
        
    def boonus(self,bonus):
        self.balance += self.bonus
        
        print(f"Balance after bonus is :{self.balance}")
       
b1=BankAccount(1000)
b1.deposit(500)
b1.withdraw(200)
b1.withdraw(2000)
        
b2=BonusAmount(1300,1000)
b2.deposit(1200)
b2.withdraw(2000)
b2.boonus(1000)
b2.withdraw(1100)
