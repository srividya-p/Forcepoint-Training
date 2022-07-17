from uuid import uuid4

class Appointment:
    allAppointments = []
    def __init__(self, patientName, doctorName, appDate, appTime, isComplete):
        self.appId = str(uuid4())
        self.patientName, self.doctorName = patientName, doctorName
        self.appDate, self.appTime = appDate, appTime
        self.isComplete = isComplete

    @staticmethod
    def createAppointment(patientName, doctorName, appDate, appTime):
        """Receptionist uses this method to create an appointment"""
        newAppointment = Appointment(patientName, doctorName, appDate, appTime, False)
        Appointment.allAppointments.append(newAppointment)
        return newAppointment

    def readAppointment(self, patientName, doctorName, appDate):
        """Receptionist uses this method to read an appointment"""
        pass

    def editAppointment(self, patientName, doctorName, appDate, property, newValue):
        """Receptionist uses this method to edit an appointment"""
        pass

    def deleteAppointment(self, patientName, doctorName, appDate):
        """Receptionist uses this method to delete an appointment"""
        pass