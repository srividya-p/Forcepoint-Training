from uuid import uuid4

class Report():
    allReports = []
    def __init__(self, patientName, doctorName, reportName, reportType, reportContents):
        self.reportId = str(uuid4())
        self.patientName = patientName
        self.doctorName = doctorName
        self.reportName = reportName
        self.reportType = reportType
        self.reportContents = reportContents
        self.isExists = True

    @staticmethod
    def findReport(reportName, patientName, doctorName):
        for report in Report.allReports:
            if (report.reportName == reportName and report.patientName == patientName 
                    and report.doctorName == doctorName and report.isExists):
                return True, report
        return False, None

    @staticmethod
    def createReport(reportName, patientName, doctorName, reportType, reportContents):
        """Receptionist uses this method to create an report"""
        reportFound, _ = Report.findReport(reportName, patientName, doctorName)
        if reportFound:
            print('This Report already exists.')
            return
        newReport = Report(reportName, patientName, doctorName, reportType, reportContents)
        Report.allReports.append(newReport)
        return newReport

    @staticmethod
    def printReport(reportName, patientName, doctorName):
        """Admin uses this method to read a receptionist"""
        reportFound, report = Report.findReport(reportName, patientName, doctorName)
        if not reportFound:
            print('This Report does not exist.')
            return
        print(f"""Report - {report.reportId} {report.patientName} 
                {report.doctorName} {report.reportName} {report.reportType} {report.reportContents}""")

    @staticmethod
    def editReport(reportName, patientName, doctorName, propertyName, newValue):
        """Admin uses this method to edit a receptionist"""
        reportFound, report = Report.findReport(reportName, patientName, doctorName)
        if not reportFound:
            print("This Report does not exist.")
            return
        
        oldValue = str(getattr(report, propertyName))
        setattr(report, propertyName, newValue)
        print(report.fullName+"'s "+propertyName+" changed from "+oldValue
                +" to "+str(getattr(report, propertyName)))

    @staticmethod
    def deleteReport(reportName, patientName, doctorName):
        """Admin uses this method to delete a receptionist"""
        reportFound, report = Report.findReport(reportName, patientName, doctorName)
        if not reportFound:
            print("This Report does not exist.")
            return

        report.isExists = False
