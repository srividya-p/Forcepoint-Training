from operator import imod
from uuid import uuid4
from user import User

class Employee(User):
    def __init__(self, userName, password, fullName, dob, age, gender, address, isAdmin, salary, funds):
        super().__init__(userName, password, fullName, dob, age, gender, address, isAdmin)
        self.salary = salary
        self.funds = funds
        self.empId = str(uuid4())

    def requestSalary():
        """Request the payroll staff to transfer salary to employee's account"""
        pass