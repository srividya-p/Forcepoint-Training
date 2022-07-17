from staff import Staff

class Payroll(Staff):
    def __init__(self, payrollUserName, password, fullName, dob, age, gender, address, isAdmin, salary, funds, role):
        super().__init__(payrollUserName, password, fullName, dob, age, gender, address, isAdmin, salary, funds, role)

    @staticmethod
    def createPayroll(payrollUserName, password, fullName, dob, age, gender, address, salary, funds, role):
        """Admin uses this method to create a staff"""
        newPayroll = Staff(payrollUserName, password, fullName, dob, age, gender, address, False, salary, funds, role)
        Staff.allStaff.append(newPayroll)
        return newPayroll

    def readPayroll(self, payrollUserName):
        """Admin uses this method to read a payroll"""
        pass

    def editPayroll(self, payrollUserName, property, newValue):
        """Admin uses this method to edit a payroll"""
        pass

    def deletePayroll(self, payrollUserName):
        """Admin uses this method to delete a payroll"""
        pass

    def giveSalary(self, employeeUserName):
        """Payroll staff transfers salary to the employee's funds"""

    def generateReport(self, reportType, reportContents):
        """Payroll staff generates and adds a report to the Report DB after paying salary"""

    def generateExpenditureReports(self):
        """Payroll staff queries all reports and generates final expenditure report"""

    