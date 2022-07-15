from sale import Sale

class Stock(Sale):
    def __init__(self, date1, date2, purchaseCode, saleDate, cName, price, quantity) -> None:
        self.date1, self.date2 = date1, date2
        super.__init__(purchaseCode, saleDate, cName, price, quantity)

    def viewStock(self):
        pass

    def cancel(self):
        pass