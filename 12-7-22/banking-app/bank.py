class Bank:
    bankId = -1
    bankList = []
    def __init__(self, bankName, bankAbbr):
        self.accountId = Bank.bankId
        self.bankName, self.bankAbbr = bankName, bankAbbr

    @staticmethod
    def createBank(bankName, bankAbbr):
        bankNameExists, _ = Bank.findBankByName(bankName)
        if bankNameExists:
            return False, "This bank name already exists!"

        bankAbbrExists, _ = Bank.findBankByAbbr(bankAbbr)
        if bankAbbrExists:
            return False, "This bank abbreviation already exists!"

        Bank.bankId += 1
        newBank = Bank(bankName, bankAbbr)
        Bank.bankList.append(newBank)
        return True, newBank

    @staticmethod
    def findBankByName(bankName):
        for bank in Bank.bankList:
            if bank.bankName == bankName:
                return True, bank

        return False, None

    @staticmethod
    def findBankByAbbr(bankAbbr):
        for bank in Bank.bankList:
            if bank.bankAbbr == bankAbbr:
                return True, bank

        return False, None