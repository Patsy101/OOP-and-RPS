from bank_accounts import * 

Patrick = BankAccount(1000, "Patrick")
Mark = BankAccount(1000,"Mark")

Patrick.getBalance()
Mark.getBalance()

# getting the balance

Patrick.deposit(500)
Mark.deposit(20)

# getting the withdraw amount
Patrick.withdraw(100)

# transferring money
Patrick.transfer(100, Mark)

#Rewards
Patrick = InterestRewardsAcct(1000, "Patrick")

Patrick.getBalance()

Patrick.deposit(100)

Patrick.transfer(100, Mark)

# Savings acct

Jean = SavingsAcct(1000, "Blaze")

Jean.getBalance()

Jean.deposit(500)

Jean.transfer(1000, Patrick)

# this could be used in personal finance 