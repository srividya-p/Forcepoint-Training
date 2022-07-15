class Purchase:
    purchaseCode = -1
    def __init__(self, productCode, stockName, purchaseQuantity, price):
        self.productCode = productCode
        self.stockName = stockName
        self.purchaseQuantity, self.price = purchaseQuantity, price
    
    @staticmethod
    def createPurchase():
        pass

    def savePurchase(self):
        pass

    def editPurchase(self):
        pass

    def deletePurchase(self):
        pass

    def exit(self):
        pass
