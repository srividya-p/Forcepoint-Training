from user import User
from receptionist import Receptionist
from login_system import LoginSystemInterface

class Patient(User):
    allPatients = []
    def __init__(self, fullName, dob, gender, address, authorizer = LoginSystemInterface):
        super().__init__(fullName, dob, gender, address ,authorizer)

    @staticmethod
    def findPatient(patientUserName):
        for patient in Patient.allPatients:
            if patient.authorizer.getUserName() == patientUserName and patient.isExists:
                return True, patient
        return False, None

    @staticmethod
    def createPatient(fullName, dob, gender, address, authorizer):
        """Admin uses this method to create a patient"""
        patientFound, _ = Patient.findPatient(authorizer.getUserName())
        if patientFound:
            print('This patient already exists.')
            return
        newPatient = Patient(fullName, dob, gender, address, authorizer)
        Patient.allPatients.append(newPatient)
        return newPatient

    @staticmethod
    def readPatient(patientUserName):
        """Admin uses this method to read a patient"""
        patientFound, patient = Patient.findPatient(patientUserName)
        if not patientFound:
            print('This patient does not exist.')
            return
        print(f"Patient - {patient.fullName} {patient.gender} {patient.address}")

    @staticmethod
    def editPatient(patientUserName, propertyName, newValue):
        """Admin uses this method to edit a patient"""
        patientFound, patient = Patient.findPatient(patientUserName)
        if not patientFound:
            print("This patient does not exist.")
            return
        
        oldValue = str(getattr(patient, propertyName))
        setattr(patient, propertyName, newValue)
        print(patient.fullName+"'s "+propertyName+" changed from "+oldValue
                +" to "+str(getattr(patient, propertyName)))

    @staticmethod
    def deletePatient(patientUserName):
        """Admin uses this method to delete a patient"""
        patientFound, patient = Patient.findPatient(patientUserName)
        if not patientFound:
            print("This patient does not exist.")
            return

        patient.isExists = False

    def requestAppointment(self, receptionistUserName, doctorUserName, date, time):
        """Request an appointment from a receptionist with a doctor"""
        receptionistFound, receptionist = Receptionist.findReceptionist(receptionistUserName)
        if not receptionistFound:
            print("This receptionist does not exist.")
            return
        receptionist.bookAppointment(self.authorizer.getUserName(), doctorUserName, date, time)

    def requestAppointmentPrintout(self, receptionistUserName, doctorUserName, date, time):
        """Request an appointment printout from a receptionist"""
        receptionistFound, receptionist = Receptionist.findReceptionist(receptionistUserName)
        if not receptionistFound:
            print("This receptionist does not exist.")
            return
        receptionist.printAppointment(self.authorizer.getUserName(), doctorUserName, date, time)

    def requestAppointmentEdit(self, receptionistUserName, doctorUserName, date, time):
        """Request an appointment edit from a receptionist"""
        receptionistFound, receptionist = Receptionist.findReceptionist(receptionistUserName)
        if not receptionistFound:
            print("This receptionist does not exist.")
            return
        receptionist.editAppointment(self.authorizer.getUserName(), doctorUserName, date, time)

    def requestAppointmentCancellation(self, receptionistUserName, doctorUserName, date, time):
        """Request an appointment cancellation from a receptionist with"""
        receptionistFound, receptionist = Receptionist.findReceptionist(receptionistUserName)
        if not receptionistFound:
            print("This receptionist does not exist.")
            return
        receptionist.cancelAppointment(self.authorizer.getUserName(), doctorUserName, date, time)

    def requestWard(self, receptionistUserName, wardName):
        """Request a receptionist for a ward and mention ward type"""
        pass

    def requestReports(self, receptionistUserName):
        """Request a receptionist to view all my test reports"""
        pass

    def viewPastAppointments(self, receptionistUserName):
        """Request a receptionist to view all my past appointments"""
        pass

    def payBill(self):
        """Pay a Bill addressed to me"""
        pass