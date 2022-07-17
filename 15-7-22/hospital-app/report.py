from uuid import uuid4

class Report():
    allReports = []
    def __init__(self, reportName, reportType, reportContents):
        self.reportId = str(uuid4())
        self.reportName = reportName
        self.reportType = reportType
        self.reportContents = reportContents

    @staticmethod
    def createReport(reportName, reportType, reportContents):
        """Admin uses this method to create a user"""
        newReport = Report(reportName, reportType, reportContents)
        Report.allUsers.append(newReport)
        return newReport

    def readReport(self, reportName):
        """Admin uses this method to read a user"""
        pass

    def editReport(self, reportName, property, newValue):
        """Admin uses this method to edit a user"""
        pass

    def deleteReport(self, reportName):
        """Admin uses this method to delete a user"""
        pass