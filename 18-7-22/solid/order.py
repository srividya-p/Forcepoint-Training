from abc import ABC, abstractmethod
# S - Single Responsibility - One class should have only one functionality
# O - Open Close Principle - A closed class should not be opened again. Implement new class
# L - Liskow's substitution principle - when sub classes don't have common method declarations, make them global vars
# I - Interface segregation principle - Separated PaymentProcessor into TFA 
# D - Dependency Inversion - No class should directly depend on a concrete class.

class Order:
    def __init__(self) -> None:
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = 'open'

    def addItem(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def totalPrice(self):
        total = 0
        for q, p in zip(self.quantities, self.prices):
            total += q*p
        return total

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order, securityCode):
        pass

# class TwoFactorAuth(PaymentProcessor):
#     @abstractmethod
#     def twoFactorAuth(self, code):
#         pass

class TwoFactorAuthInterface(ABC):
    @abstractmethod
    def verifyCode(self, code):
        pass

    @abstractmethod
    def isVerified(self):
        pass

class TwoFactorAuth(TwoFactorAuthInterface):
    def __init__(self) -> None:
        self.verified = False

    def verifyCode(self, code):
        #Code check
        self.verified = True

    def isVerified(self):
        return self.verified

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, securityCode, authorizer = TwoFactorAuthInterface):
        super().__init__()
        self.securityCode = securityCode
        self.verified = False
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.isVerified(): raise Exception("Payment not verified.")
        print("Processing debit card payment...")
        print(f"Verifying security code {self.securityCode}")
        order.status = 'paid'

    # def twoFactorAuth(self, code):
    #     print(f'Verified using {code}')
    #     self.verified = True

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, securityCode, authorizer = TwoFactorAuthInterface):
        super().__init__()
        self.securityCode = securityCode
        self.verified = False
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.isVerified(): raise Exception("Payment not verified.")
        print("Processing credit card payment...")
        print(f"Verifying security code {self.securityCode}")
        order.status = 'paid'

    # def twoFactorAuth(self, code):
    #     print(f'Verified using {code}')
    #     self.verified = True

class UPIPaymentProcessor(PaymentProcessor):
    def __init__(self, upiId):
        super().__init__()
        self.upiId = upiId
        self.verified = False

    def pay(self, order):
        print("Processing UPI payment...")
        print(f"Verifying security code {self.upiId}")
        order.status = 'paid'

    
o = Order()
o.addItem('A', 1, 500)
o.addItem('B', 2, 600)
o.addItem('C', 4, 800)
print(o.totalPrice())

p = DebitPaymentProcessor('12345', TwoFactorAuth())
p.authorizer.verifyCode('2424')
p.pay(o)