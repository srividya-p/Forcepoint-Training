from uuid import uuid4

class Ward:
    allWards = []
    def __init__(self, wardName, occupancySize, wardType, isOccupied, currentPatient):
        self.wardId = str(uuid4())
        self.wardName = wardName
        self.occupancySize, self.wardType = occupancySize, wardType
        self.isOccupied = isOccupied
        self.currentPatient = currentPatient

    @staticmethod
    def createWard(wardName, occupancySize, wardType, currentPatient):
        """Admin uses this method to create a ward"""
        newWard = Ward(wardName, occupancySize, wardType, False, currentPatient)
        Ward.allAppointments.append(newWard)
        return newWard

    def readWard(self,):
        """Admin uses this method to read a ward"""
        pass

    def editWard(self, wardName, property, newValue):
        """Admin uses this method to edit a ward"""
        pass

    def deleteWard(self, wardName):
        """Admin uses this method to delete a ward"""
        pass