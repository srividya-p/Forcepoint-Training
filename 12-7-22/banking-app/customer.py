from bank import Bank
from account import Account

class Customer:
    customerId = -1
    customerList = []
    def __init__(self, userName, firstName, lastName, totalBalance, accounts):
        self.userName = userName
        self.customerId = Customer.customerId
        self.firstName, self.lastName = firstName, lastName
        self.totalBalance = totalBalance
        self.accounts = accounts

    @staticmethod
    def createCustomer(userName, firstName, lastName):
        customerExists, _ = Customer.findCustomer(userName)
        if customerExists:
            return False, "Cannot create customer! Username already exists."
        
        Customer.customerId += 1
        newCustomer = Customer(userName, firstName, lastName, 0, [])
        Customer.customerList.append(newCustomer)
        return True, newCustomer

    @staticmethod
    def findCustomer(userName):
        for customer in Customer.customerList:
            if customer.userName == userName:
                return True, customer

        return False, None

    def findAccount(self, bankAbbr):
        for account in self.accounts:
            if account.getBankAbbr() == bankAbbr:
                return True, account

        return False, None

    def __updateTotalBalance(self):
        self.totalBalance = 0
        for account in self.accounts:
            self.totalBalance += account.balance

    def createAccount(self, bankAbbr):
        bankAbbrExists, bank = Bank.findBankByAbbr(bankAbbr)
        if not bankAbbrExists:
            return False, "This bank does not exist!"

        accountExists, _ = self.findAccount(bankAbbr)
        if accountExists:
            return False, "You already have an account with this bank!"

        self.accounts.append(Account.createAccount(bank))
        self.__updateTotalBalance()
        return True, "Account created successfully."

    def displayBalance(self):
        print("Total Balance = " + str(self.totalBalance))
        print("Account Balances:")
        for account in self.accounts:
            print(account.getBankName() + " " + account.getBankAbbr() + " " + str(account.balance))

    def withdraw(self, bankAbbr, amount):
        accountExists, account = self.findAccount(bankAbbr)
        if not accountExists:
            return False, "This account does not exist!"

        if account.balance < amount:
            return False, "Insufficient balance!"

        account.balance -= amount
        self.__updateTotalBalance()
        return True, "Amount withdrawn successfully."

    def deposit(self, bankAbbr, amount):
        accountExists, account = self.findAccount(bankAbbr)
        if not accountExists:
            return False, "This account does not exist!"

        account.balance += amount
        self.__updateTotalBalance()
        return True, "Amount deposited successfully."


    def transfer(self, creditBankAbbr, creditUserName, debitBankAbbr, amount):
        self.withdraw(debitBankAbbr, amount)

        creditUserExists, creditUser = Customer.findCustomer(creditUserName)
        if not creditUserExists:
            return False, "The credit user does not exist."

        creditUser.deposit(creditBankAbbr, amount)
        return True, "Transferred amount successfully."

    def selfTransfer(self, creditBankAbbr, debitBankAbbr, amount):
        self.withdraw(debitBankAbbr, amount)
        self.deposit(creditBankAbbr, amount)
        return True, "Transferred (self) amount successfully."

    def getCustomerName(self):
        return self.firstName + " " + self.lastName