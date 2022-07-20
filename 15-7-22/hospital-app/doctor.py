from employee import Employee
from staff import Staff
from login_system import LoginSystemInterface

class Doctor(Employee):
    allDoctors = []
    def __init__(self, fullName, dob, gender, address, isAdmin, salary, funds, yearsOfExp, doctorType, authorizer = LoginSystemInterface):
        super().__init__(fullName, dob, gender, address, isAdmin, salary, funds, authorizer)
        self.yearsOfExp = yearsOfExp
        self.doctorType = doctorType
    
    @staticmethod
    def findDoctor(doctorUserName):
        for doctor in Doctor.allDoctors:
            if doctor.authorizer.getUserName() == doctorUserName and doctor.isExists:
                return True, doctor
        return False, None

    @staticmethod
    def createDoctor(fullName, dob, gender, address, salary, funds, yearsOfExp, doctorType, authorizer):
        """Admin uses this method to create a doctor"""
        doctorFound, _ = Doctor.findDoctor(authorizer.getUserName())
        if doctorFound:
            print('This doctor already exists.')
            return
        newDoctor = Doctor(fullName, dob, gender, address, salary, funds, yearsOfExp, doctorType, authorizer)
        Doctor.allDoctors.append(newDoctor)
        return newDoctor

    @staticmethod
    def readDoctor(doctorUserName):
        """Admin uses this method to read a doctor"""
        doctorFound, doctor = Doctor.findDoctor(doctorUserName)
        if not doctorFound:
            print('This doctor does not exist.')
            return
        print(f"Doctor - {doctor.fullName} {doctor.gender} {doctor.address} {doctor.doctorType} {doctor.yearsOfExp}")

    @staticmethod
    def editDoctor(doctorUserName, propertyName, newValue):
        """Admin uses this method to edit a doctor"""
        doctorFound, doctor = Doctor.findDoctor(doctorUserName)
        if not doctorFound:
            print("This doctor does not exist.")
            return
        
        oldValue = str(getattr(doctor, propertyName))
        setattr(doctor, propertyName, newValue)
        print(doctor.fullName+"'s "+propertyName+" changed from "+oldValue
                +" to "+str(getattr(doctor, propertyName)))

    @staticmethod
    def deleteDoctor(doctorUserName):
        """Admin uses this method to delete a doctor"""
        doctorFound, doctor = Doctor.findDoctor(doctorUserName)
        if not doctorFound:
            print("This doctor does not exist.")
            return

        doctor.isExists = False

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
        isStaffPresent, staff = Staff.findStaff(staffUsername)
        if not isStaffPresent:
            print('This staff does not exist.')
            return
        staff.addDoctorTask(self.authorizer.getUserName(), task)