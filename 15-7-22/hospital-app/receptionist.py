from staff import Staff
from bill import Bill
from appointment import Appointment
from report import Report
from login_system import LoginSystemInterface

class Receptionist(Staff):
    allReceptionists = []
    def __init__(self, fullName, dob, gender, address, salary, funds, role, authorizer = LoginSystemInterface):
        super().__init__(fullName, dob, gender, address, salary, funds, role, authorizer)

    @staticmethod
    def findReceptionist(receptionistUserName):
        for receptionist in Receptionist.allReceptionists:
            if receptionist.authorizer.getUserName() == receptionistUserName and receptionist.isExists:
                return True, receptionist
        return False, None
    
    @staticmethod
    def createReceptionist(fullName, dob, gender, address, salary, funds, role, authorizer):
        """Admin uses this method to create a receptionist"""
        receptionistFound, _ = Receptionist.findReceptionist(authorizer.getUserName())
        if receptionistFound:
            print('This receptionist already exists.')
            return
        newReceptionist = Receptionist(fullName, dob, gender, address, salary, funds, role, authorizer)
        Receptionist.allUsers.append(newReceptionist)
        return newReceptionist
    
    @staticmethod
    def readReceptionist(receptionistUserName):
        """Admin uses this method to read a receptionist"""
        receptionistFound, receptionist = Receptionist.findReceptionist(receptionistUserName)
        if not receptionistFound:
            print('This receptionist does not exist.')
            return
        print(f"Receptionist - {receptionist.fullName} {receptionist.gender} {receptionist.address} {receptionist.role}")

    @staticmethod
    def editReceptionist(receptionistUserName, propertyName, newValue):
        """Admin uses this method to edit a receptionist"""
        receptionistFound, receptionist = Receptionist.findReceptionist(receptionistUserName)
        if not receptionistFound:
            print("This receptionist does not exist.")
            return
        
        oldValue = str(getattr(receptionist, propertyName))
        setattr(receptionist, propertyName, newValue)
        print(receptionist.fullName+"'s "+propertyName+" changed from "+oldValue
                +" to "+str(getattr(receptionist, propertyName)))

    @staticmethod
    def deleteReceptionist(receptionistUserName):
        """Admin uses this method to delete a receptionist"""
        receptionistFound, receptionist = Receptionist.findReceptionist(receptionistUserName)
        if not receptionistFound:
            print("This receptionist does not exist.")
            return

        receptionist.isExists = False

    def bookAppointment(self, patientUserName, doctorUserName, appDate, appTime):
        Appointment.createAppointment(patientUserName, doctorUserName, appDate, appTime)
        self.generateBill(patientUserName, 1000)

    def printAppointment(patientUserName, doctorUserName, appDate, appTime):
        Appointment.printAppointment(patientUserName, doctorUserName, appDate, appTime)

    def editAppointment(self, patientUserName, doctorUserName, appDate, appTime, propertyName, newValue):
        Appointment.editAppointment(patientUserName, doctorUserName, appDate, appTime, propertyName, newValue)
    
    def cancelAppointment(self, patientUserName, doctorUserName, appDate, appTime):
        Appointment.deleteAppointment(patientUserName, doctorUserName, appDate, appTime)

    def generateBill(self, patientUserName, amount):
        Bill.createBill(patientUserName, amount)

    def cancelBill(self):
        pass

    def bookWard(self):
        pass #How to fix circular import?

    def fetchReports(self):
        pass

    def fetchAppointments(self):
        pass

