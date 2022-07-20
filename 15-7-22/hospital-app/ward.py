from uuid import uuid4
from patient import Patient

class Ward:
    allWards = []
    def __init__(self, wardName, occupancySize, wardType, isOccupied, currentPatient):
        self.wardId = str(uuid4())
        self.wardName = wardName
        self.occupancySize, self.wardType = occupancySize, wardType
        self.isOccupied = isOccupied
        self.currentPatient = currentPatient
        self.isExists = True

    @staticmethod
    def findWard(wardName):
        for ward in Ward.allWards:
            if ward.authorizer.getUserName() == wardName and ward.isExists:
                return True, ward
        return False, None

    @staticmethod
    def updateWardTypeAggregation():
        pass

    @staticmethod
    def createWard(wardName, occupancySize, wardType, currentPatient):
        """Admin uses this method to create a ward"""
        wardFound, _ = Ward.findWard(wardName)
        if wardFound:
            print('This ward already exists.')
            return
        newWard = Ward(wardName, occupancySize, wardType, currentPatient)
        Ward.allWards.append(newWard)
        Ward.updateWardTypeAggregation(wardType)
        return newWard

    @staticmethod
    def readWard(wardName):
        """Admin uses this method to read a ward"""
        wardFound, ward = Ward.findWard(wardName)
        if not wardFound:
            print('This ward does not exist.')
            return
        print(f"Ward - {ward.wardName} {ward.occupancySize} {ward.wardType} {ward.currentPatient}")

    @staticmethod
    def editWard(wardName, propertyName, newValue):
        """Admin uses this method to edit a ward"""
        wardFound, ward = Ward.findWard(wardName)
        if not wardFound:
            print("This ward does not exist.")
            return
        
        oldValue = str(getattr(ward, propertyName))
        setattr(ward, propertyName, newValue)
        print(ward.fullName+"'s "+propertyName+" changed from "+oldValue
                +" to "+str(getattr(ward, propertyName)))

    @staticmethod
    def deleteWard(wardName):
        """Admin uses this method to delete a ward"""
        wardFound, ward = Ward.findWard(wardName)
        if not wardFound:
            print("This ward does not exist.")
            return

        ward.isExists = False

    def getCurrentPatientDetails(self):
        pass