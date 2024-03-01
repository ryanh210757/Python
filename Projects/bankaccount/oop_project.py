from bank_accounts import *

Ryan = BankAccount(1000, "Ryan")
Adryanna = BankAccount(5000, "Adryanna")

Ryan.get_balance()
Adryanna.get_balance()

Ryan.deposit(300)
Adryanna.deposit(250)

Ryan.withdraw(1100)


Ryan.transfer(50, Adryanna)
Ryan.transfer(50, Adryanna)

Jimmy = InterestRewardsAcct(1000, "Jim")
Jimmy.get_balance()
Jimmy.deposit(100)
Jimmy.transfer(100, Ryan)
Jimmy.transfer(5, Ryan)

Blaze = SavingsAcct(100, "Blaze")
Blaze.get_balance()
Blaze.deposit(100)
Blaze.transfer(10000, Adryanna)
