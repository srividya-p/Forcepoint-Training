class SalaryRequest:
    def __init__(self, employeeUsername, amount) -> None:
        self.employeeUsername = employeeUsername
        self.amount = amount
        self.isProcessed = False

class SalaryRequestManager:
    allSalaryRequests = []
    hospitalFunds = 0
    taxPercent = 0

    def __init__(self):
        pass

    @staticmethod
    def addSalaryRequest(employeeUsername, amount):
        newSalaryRequest = SalaryRequest(employeeUsername, amount)
        SalaryRequestManager.allSalaryRequests.append(newSalaryRequest)
        print('Salary Request added.')
        return SalaryRequestManager.processSalaryRequest(newSalaryRequest)

    @staticmethod
    def processSalaryRequest(salaryRequest):
        print('Processing salary request...')
        creditAmount = salaryRequest.amount - salaryRequest.amount * (SalaryRequestManager.taxPercent / 100)
        if SalaryRequestManager.hospitalFunds < creditAmount:
            print('The hospital does not have enough money to pay salary now.')
            return False, 0
        salaryRequest.isProcessed = True
        return True, creditAmount

    @staticmethod
    def setHospitalFunds(amount):
        """Admin can set funds"""
        SalaryRequestManager.hospitalFunds = amount

    @staticmethod
    def setTaxPercent(percent):
        """Admin can set tax percent"""
        SalaryRequestManager.taxPercent = percent

        

        

    