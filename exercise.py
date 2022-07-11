from datetime import date, datetime

class Student():
    def __init__(self, firstName, lastName, fullName,
                    admitYear, gradYear, dropYears, dob, age, gpaSems, gradeSems, cgpa, grade):
        self.lastName = lastName
        self.firstName = firstName
        self.fullName = fullName
        self.admitYear = admitYear
        self.gradYear = gradYear
        self.dropYears = dropYears
        self.dob, self.age = dob, age
        self.gpaSems, self.gradeSems = gpaSems, gradeSems
        self.cgpa, self.grade = cgpa, grade

    @staticmethod
    def initStudent(firstName, lastName, admitYear, gradYear, dob, gpaSems):
        def getGrade(gpa):
            if gpa >= 8: return 'A'
            elif gpa < 8 and gpa >= 6: return 'B'
            elif gpa <6 and gpa >= 3: return 'C'
            else: return 'D'

        fullName = firstName+" "+lastName
        dropYears = gradYear - admitYear - 4
        d, m, y = [int(n) for n in dob.split('/')]
        today = date.today()
        age = today.year - y - ((today.month, today.day) < (m, d))
        gradeSems = [getGrade(gpa) for gpa in gpaSems]
        cgpa = sum(gpaSems) / len(gpaSems)
        grade = getGrade(cgpa)

        return Student(firstName, lastName, fullName,
                    admitYear, gradYear, dropYears, dob, age, gpaSems, gradeSems, cgpa, grade)
           
    def show(self, propertyName):
        print("Student - "+self.fullName+"'s "+propertyName+" is "+str(getattr(self, propertyName)))

    def update(self, propertyName, newValue):
        oldValue = str(getattr(self, propertyName))
        setattr(self, propertyName, newValue)
        print("Student - "+self.fullName+"'s "+propertyName+" changed from "+oldValue
                +" to "+str(getattr(self, propertyName)))

me = Student.initStudent('Srividya', 'Subramanian', 2018, 2022, '24/4/2001', [9, 8, 8, 9, 8, 7, 9, 10])

action = input("Enter action (S/U) - ")

try:
    if(action == 'S'):
        me.show(input("Enter property name - "))
    else:
        me.update(input("Enter property name - "), input("Enter new value - "))
except AttributeError:
    print("This property does not exist!")
