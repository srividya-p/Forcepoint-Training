from abc import ABC, abstractclassmethod


from abc import ABC

class IShippingCompany(ABC):
    @abstractclassmethod
    def calculateBill(self, amount):
        pass

class Fedex(IShippingCompany):
    def calculateBill(self, amount):
        return amount * 10

class DTDC(IShippingCompany):
    def calculateBill(self, amount):
        return amount * 15

class MyCompany(IShippingCompany):
    def calculateBill(self, amount):
        pass