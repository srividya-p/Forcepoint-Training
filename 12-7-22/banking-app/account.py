class Account():
    accountId = -1
    def __init__(self, bank, balance):
        self.accountId = Account.accountId
        self.bank = bank
        self.balance = balance

    @staticmethod
    def createAccount(bank):
        Account.accountId += 1
        return Account(bank, 1000)

    def getBankName(self):
        return self.bank.bankName

    def getBankAbbr(self):
        return self.bank.bankAbbr