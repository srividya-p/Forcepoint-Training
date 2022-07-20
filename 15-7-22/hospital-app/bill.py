from uuid import uuid4

class Bill:
    allBills = []
    def __init__(self, amount, payerUserName, isPaid):
        self.billId = str(uuid4())
        self.amount, self.payerUserName = amount, payerUserName
        self.isPaid = isPaid
        self.isExists = True

    @staticmethod
    def findBill(amount, payerUserName, isPaid):
        for bill in Bill.allStaff:
            if (bill.amount == amount and bill.payerUserName == payerUserName and 
                    bill.isPaid == isPaid and bill.isExists == True):
                return True, bill
        return False, None

    @staticmethod
    def createBill(amount, payerUserName):
        """Receptionist uses this method to create a bill"""
        billFound, _ = Bill.findBill(amount, payerUserName, False)
        if not billFound:
            print('This bill already exists.')
            return
        newBill = Bill(amount, payerUserName, False)
        Bill.allBills.append(newBill)
        return newBill

    @staticmethod
    def printBill(amount, payerUserName, isPaid):
        """Admin uses this method to read a staff"""
        billFound, bill = Bill.findBill(amount, payerUserName, isPaid)
        if not billFound:
            print('This staff member does not exist.')
            return
        print(f"Bill ID {bill.billId} - {bill.payerUserName} {bill.amount} {'PAID' if bill.isPaid else 'PENDING'}")

    @staticmethod
    def deleteBill(amount, payerUserName, isPaid):
        """Receptionist uses this method to delete a bill"""
        billFound, bill = Bill.findBill(amount, payerUserName, isPaid)
        if not billFound:
            print("This bill does not exist.")
            return

        bill.isExists = False

