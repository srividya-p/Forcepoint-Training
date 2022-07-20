from employee import Employee
from login_system import LoginSystemInterface

class Task:
    def __init__(self, doctorUserName, taskName, isComplete):
        self.doctorUserName = doctorUserName
        self.taskName = taskName
        self.isComplete = isComplete

class Staff(Employee):
    allStaff = []
    def __init__(self, fullName, dob, gender, address, salary, funds, role, authorizer = LoginSystemInterface):
        super().__init__(fullName, dob, gender, address, salary, funds, authorizer)
        self.role = role
        self.tasks = []

    @staticmethod
    def findStaff(staffUserName):
        for staff in Staff.allStaff:
            if staff.authorizer.getUserName() == staffUserName and staff.isExists:
                return True, staff
        return False, None

    @staticmethod
    def createStaff(fullName, dob, gender, address, salary, funds, role, authorizer):
        """Admin uses this method to create a staff"""
        staffFound, _ = Staff.findStaff(authorizer.getUserName())
        if staffFound:
            print('This Staff already exists.')
            return
        newStaff = Staff(fullName, dob, gender, address, salary, funds, role, authorizer)
        Staff.allStaff.append(newStaff)
        return newStaff

    @staticmethod
    def readStaff(staffUserName):
        """Admin uses this method to read a staff"""
        staffFound, staff = Staff.findStaff(staffUserName)
        if not staffFound:
            print('This staff member does not exist.')
            return
        print(f"Staff - {staff.fullName} {staff.dob} {staff.gender} {staff.address} {staff.role}")

    @staticmethod
    def editStaff(staffUserName, propertyName, newValue):
        """Admin uses this method to edit a staff"""
        staffFound, staff = Staff.findStaff(staffUserName)
        if not staffFound:
            print("This staff member does not exist.")
            return
        
        oldValue = str(getattr(staff, propertyName))
        setattr(staff, propertyName, newValue)
        print(staff.fullName+"'s "+propertyName+" changed from "+oldValue
                +" to "+str(getattr(staff, propertyName)))

    @staticmethod
    def deleteStaff(staffUserName):
        """Admin uses this method to delete a staff"""
        staffFound, staff = Staff.findStaff(staffUserName)
        if not staffFound:
            print("This staff member does not exist.")
            return

        staff.isExists = False

    def findTask(self, doctorUserName, taskName):
        for task in self.tasks:
            if task.doctorUserName == doctorUserName and task.taskName == taskName:
                return True, task
        return False, None
    
    def addDoctorTask(self, doctorUserName, taskName):
        """Add a task assigned by a doctor."""
        taskFound, task = self.findTask(doctorUserName, taskName)
        if taskFound:
            print('This task was already added.')
            return
        self.tasks.append(Task(doctorUserName, taskName, False))
        print('Task added successfully.')

    def performTask(self, doctorUserName, taskName):
        """Perform a task assigned by a particular doctor"""
        taskFound, task = self.findTask(doctorUserName, taskName)
        if not taskFound:
            print('This task does not exist.')
            return
        task.isComplete = True
        print('Task completed.')

