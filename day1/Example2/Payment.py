from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        print("Payment abstract method")
        pass

# TypeError: Can't instantiate abstract class Payment 
# with abstract method pay

# pay = Payment()
# print(pay)
