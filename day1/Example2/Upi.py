from Payment import Payment

class UPI(Payment):
    def pay(self, amount):
        super().pay(self)
        print(f"Paid {amount} via UPI")
