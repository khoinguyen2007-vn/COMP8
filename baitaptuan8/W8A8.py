class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def withdraw(self,wd):
        if wd <= self.balance:
            self.balance -= wd
        return self.balance
    def deposit(self,dp):
        self.balance += dp
        return self.balance
o,b = input().split()
res = 0
ba = BankAccount(o,float(b))
n = int(input())
for i in range(n):
    y,z = input().split()
    if y == "DEPOSIT":
        res = ba.deposit(float(z))
    else:
        res = ba.withdraw(float(z))
print(f'{res:.2f}')
