from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


# This follows Dependency Injection + Interface Design
def process_payment(payment: Payment):
    payment.pay(1000)

process_payment(UpiPayment()) # Paid 1000 using UPI
process_payment(CreditCardPayment()) # Paid 1000 using Credit Card