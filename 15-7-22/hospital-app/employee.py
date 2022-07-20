from operator import imod
from uuid import uuid4
from user import User
from login_system import LoginSystemInterface
from salary_request_manager import SalaryRequestManager 

class Employee(User):
    def __init__(self, fullName, dob, gender, address, salary, funds, authorizer = LoginSystemInterface):
        super().__init__(fullName, dob, gender, address, authorizer)
        self.empId = str(uuid4())
        self.salary = salary
        self.funds = funds

    def requestSalary(self):
        """Add a salary request and update funds"""
        if not self.authorizer.isLoggedIn():
            print('You are not logged in!')
            return

        isProcessed, creditAmount = SalaryRequestManager.addSalaryRequest(self.authorizer.getUserName(), self.salary)
        if not isProcessed:
            print('Salary request was not processed! Try again later.')
            return

        self.funds += creditAmount
        print('Salary request processed successfully.')
        