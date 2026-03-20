from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class CreditCard(Payment):
    def process(self, amount):
        print(f"Connecting to Visa Portal .. Charged ${amount}")

class Paypal(Payment):
    def process(self, amount):
        print(f"Connecting to PayPal .. Paid ${amount}")

def checkout(payment_method,cost):
    payment_method.process(cost)

checkout(CreditCard(),100)
checkout(Paypal(),200)