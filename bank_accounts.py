class BalanceException(Exception):
    pass

class BankAccount:
    def __init__ (self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
    
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = $ {self.balance:.2f}")
        
    # getting balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nsuccessfully deposited")
        self.getBalance()
        
    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account  '{self.name}' only has a balance of ${self.balance:.2f}"
            )
    def withdraw (self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\n Withdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
            
    def transfer(self, amount, account):
        try:
            print('\n********\n\n Beginning Transfer..')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete! Matewa!')
        except BalanceException as error:
            print(f'\nTransfer interrupted . {error}')
            
class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + amount * 1.05
        print("\nDeposit done.")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self,initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5
        
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed")
            self.getBalance
        except BalanceException as error:
            print(f'\n Withdraw interrupted: {error}')
        
    