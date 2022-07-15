class Sale:
    def __init__(self, purchaseCode, saleDate, cName, price, quantity):
        self.saleDate, self.cName = saleDate, cName
        self.purchaseCode = purchaseCode
        self.price, self.quantity = price, quantity

    def addSales(self):
        pass

    def exit(self):
        pass