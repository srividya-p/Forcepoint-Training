from employee import Employee

class Staff(Employee):
    allStaff = []
    def __init__(self, staffUserName, password, fullName, dob, age, gender, address, isAdmin, salary, funds, role):
        super().__init__(staffUserName, password, fullName, dob, age, gender, address, isAdmin, salary, funds)
        self.role = role
        self.tasks = []

    @staticmethod
    def createStaff(staffUserName, password, fullName, dob, age, gender, address, salary, funds, role):
        """Admin uses this method to create a staff"""
        newStaff = Staff(staffUserName, password, fullName, dob, age, gender, address, False, salary, funds, role)
        Staff.allStaff.append(newStaff)
        return newStaff

    def readStaff(self, staffUserName):
        """Admin uses this method to read a staff"""
        pass

    def editStaff(self, staffUserName, property, newValue):
        """Admin uses this method to edit a staff"""
        pass

    def deleteStaff(self, staffUserName):
        """Admin uses this method to delete a staff"""
        pass

    def performTask(self, doctorUserName, taskName):
        """Perform a task assigned by a particular doctor"""
        pass