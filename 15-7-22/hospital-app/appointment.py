from uuid import uuid4

class Appointment:
    allAppointments = []
    def __init__(self, patientUserName, doctorUserName, appDate, appTime, isComplete):
        self.appId = str(uuid4())
        self.patientUserName, self.doctorUserName = patientUserName, doctorUserName
        self.appDate, self.appTime = appDate, appTime
        self.isComplete = isComplete
        self.isExists = True

    @staticmethod
    def findAppointment(patientUserName, doctorUserName, appDate, appTime):
        for appointment in Appointment.allAppointments:
            if (appointment.patientUserName == patientUserName and appointment.doctorUserName == doctorUserName and 
                appointment.appDate == appDate and appointment.appTime == appTime and appointment.isExists):
                return True, appointment
        return False, None

    @staticmethod
    def createAppointment(patientUserName, doctorUserName, appDate, appTime):
        """Receptionist uses this method to create an appointment"""
        appFound, _ = Appointment.findAppointment(patientUserName, doctorUserName, appDate, appTime)
        if appFound:
            print('This Appointment already exists.')
            return
        newAppointment = Appointment(patientUserName, doctorUserName, appDate, appTime, False)
        Appointment.allAppointments.append(newAppointment)
        return newAppointment

    @staticmethod
    def printAppointment(patientUserName, doctorUserName, appDate, appTime):
        """Admin uses this method to read a receptionist"""
        appFound, appointment = Appointment.findAppointment(patientUserName, doctorUserName, appDate, appTime)
        if not appFound:
            print('This receptionist does not exist.')
            return
        print(f"""Appointment - {appointment.appId} {appointment.patientUserName} 
                {appointment.doctorUserName} {appointment.appDate} {appointment.appTime}""")

    @staticmethod
    def editAppointment(patientUserName, doctorUserName, appDate, appTime, propertyName, newValue):
        """Admin uses this method to edit a receptionist"""
        appFound, appointment = Appointment.findAppointment(patientUserName, doctorUserName, appDate, appTime)
        if not appFound:
            print("This receptionist does not exist.")
            return
        
        oldValue = str(getattr(appointment, propertyName))
        setattr(appointment, propertyName, newValue)
        print(appointment.fullName+"'s "+propertyName+" changed from "+oldValue
                +" to "+str(getattr(appointment, propertyName)))

    @staticmethod
    def deleteAppointment(patientUserName, doctorUserName, appDate, appTime):
        """Admin uses this method to delete a receptionist"""
        appFound, appointment = Appointment.findAppointment(patientUserName, doctorUserName, appDate, appTime)
        if not appFound:
            print("This receptionist does not exist.")
            return

        appointment.isExists = False