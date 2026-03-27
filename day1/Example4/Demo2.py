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
    
    def __str__(self):
        return f"{self.owner} ({self._balance})"


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
800
Account(owner='Uday', balance=800) # __str__ not defined
Account(owner='Uday', balance=800)

800
'Uday' (800)                       # __str__ is defined
Account(owner='Uday', balance=800)
'''