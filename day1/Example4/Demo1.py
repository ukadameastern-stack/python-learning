from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass

    @property
    def balance(self):
        return self._balance

    def __repr__(self):
        return f"Account(owner={self.owner!r}, balance={self._balance!r})"
    

class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount


acc = SavingsAccount("Uday", 1000)
acc.withdraw(200)

print(acc.balance)   # property
print(acc)           # __repr__
print(repr(acc))     # explicit → __repr__

'''
Without: !r
800
Account(owner=Uday, balance=800)
Account(owner=Uday, balance=800)

With: !r
800
Account(owner='Uday', balance=800)
Account(owner='Uday', balance=800)
'''