from user import User

class Patient(User):
    allPatients = []
    def __init__(self, patientUserName, password, fullName, dob, age, gender, address, isAdmin):
        super().__init__(patientUserName, password, fullName, dob, age, gender, address, isAdmin)

    @staticmethod
    def createPatient(patientUserName, password, fullName, dob, age, gender, address):
        """Admin uses this method to create a patient"""
        newPatient = Patient(patientUserName, password, fullName, dob, age, gender, address, False)
        Patient.allPatients.append(newPatient)
        return newPatient

    def readPatient(self, patientUserName):
        """Admin uses this method to read a patient"""
        pass

    def editPatient(self, patientUserName, property, newValue):
        """Admin uses this method to edit a patient"""
        pass

    def deletePatient(self, patientUserName):
        """Admin uses this method to delete a patient"""
        pass

    def requestAppointment(self, receptionistUserName, doctorUserName):
        """Request an appointment from a receptionist with a doctor"""
        pass

    def requestWard(self, receptionistUserName, wardType):
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