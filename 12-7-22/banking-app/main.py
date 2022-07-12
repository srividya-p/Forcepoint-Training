from calendar import c
from customer import Customer
from bank import Bank

def showAccounts(*args):
    for c in args:
        print('\n'+c.getCustomerName())
        c.displayBalance()

print('\nCREATION OF CUSTOMERS, BANKS AND ACCOUNTS')
_, c1 = Customer.createCustomer('pikachu', 'Srividya', 'Subramanian')
_, c2 = Customer.createCustomer('charmander', 'Archit', 'Bhonsle')
_, c3 = Customer.createCustomer('bulbasaur', 'Sara', 'Varghese')

# Check unique
_, err = Customer.createCustomer('bulbasaur', 'Anya', 'Gupta')
print(err)

_, b1 = Bank.createBank('State Bank of India', 'SBI')
_, b2 = Bank.createBank('Bank of Baroda', 'BOB')
_, b3 = Bank.createBank('Punjab National Bank', 'PNB')
_, b4 = Bank.createBank('Hello Dungeon Festival Caramel', 'HDFC')

# Check unique
_, err = Bank.createBank('Lorem Ipsum', 'HDFC')
print(err)
_, err = Bank.createBank('Bank of Baroda', 'BON')
print(err)

print(c1.createAccount('SBI')[1])
print(c1.createAccount('BOB')[1])
print(c2.createAccount('PNB')[1])
print(c2.createAccount('HDFC')[1])
print(c3.createAccount('BOB')[1])
print(c3.createAccount('HDFC')[1])

# Check unique
_, err = c1.createAccount('SBI')
print(err)

# Check Bank not exists
_, err = c1.createAccount('SBU')
print(err)

print('\n\nDISPLAYING ACCOUNT DETAILS AND BALANCE', end = " ")
showAccounts(c1, c2, c3)

print('\n\nDEPOSIT, WITHDRAW, TRANSFER, SELF TRANSFER')
print(c1.deposit('SBI', 1000)[1])
print(c1.withdraw('BOB', 500)[1])
showAccounts(c1)

# Check Account exists
_, err = c1.deposit('HDFC', 1000)
print('\n'+err)

#Check insufficient balance
_, err = c1.withdraw('BOB', 2000)
print(err)

print(c2.transfer('BOB', 'pikachu', 'PNB', 500)[1])

print(c3.selfTransfer('BOB', 'HDFC', 700)[1])

print('\n\nSTATUS OF ACCOUNTS AFTER TRANSACTIONS', end = "")
showAccounts(c1, c2, c3)