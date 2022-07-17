from uuid import uuid4

class MedicalTest:
    def __init__(self, testType, doctorUserName, patientUserName):
        self.testId = str(uuid4())
        self.testType = testType
        self.doctorUserName = doctorUserName
        self.patientUserName = patientUserName

    def generateReport(self):
        pass