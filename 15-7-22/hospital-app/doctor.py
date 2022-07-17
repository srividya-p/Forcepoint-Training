from employee import Employee

class Doctor(Employee):
    allDoctors = []
    def __init__(self, doctorUserName, password, fullName, dob, age, gender, address, isAdmin, salary, funds, yearsOfExp, doctorType):
        super().__init__(doctorUserName, password, fullName, dob, age, gender, address, isAdmin, salary, funds)
        self.yearsOfExp = yearsOfExp
        self.doctorType = doctorType

    @staticmethod
    def createDoctor(doctorUserName, password, fullName, dob, age, gender, address, salary, funds, yearsOfExp, doctorType):
        """Admin uses this method to create a doctor"""
        newDoctor = Doctor(doctorUserName, password, fullName, dob, age, gender, address, False, salary, funds, yearsOfExp, doctorType)
        Doctor.allDoctors.append(newDoctor)
        return newDoctor

    def readDoctor(self, doctorUserName):
        """Admin uses this method to read a doctor"""
        pass

    def editDoctor(self, doctorUserName, property, newValue):
        """Admin uses this method to edit a doctor"""
        pass

    def deleteDoctor(self, doctorUserName):
        """Admin uses this method to delete a doctor"""
        pass 

    def handleAppointment(self, doctorUserName): 
        """Handle an appointment for a Patient"""
        pass

    def generatePatientReport(self, patientUserName):
        """Add a prescription report in Report database"""
        pass

    def recommendTest(self, patientUserName, testType):
        """Recommend a medical test to a Patient"""
        pass

    def assignStaffTask(self, staffUsername, task):
        """Assign a task to a hospital staff member"""
        pass