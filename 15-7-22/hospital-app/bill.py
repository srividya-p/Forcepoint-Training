from uuid import uuid4

class Bill:
    allBills = []
    def __init__(self, amount, payerUserName, isPaid):
        self.billId = str(uuid4())
        self.amount, self.payerUserName = amount, payerUserName
        self.isPaid = isPaid

    @staticmethod
    def createBill(amount, payerUserName):
        """Receptionist uses this method to create a bill"""
        newBill = Bill(amount, payerUserName, False)
        Bill.allBills.append(newBill)
        return newBill

    def deleteBill(self, amount, payerUserName, isPaid):
        """Receptionist uses this method to delete a bill"""
        pass

