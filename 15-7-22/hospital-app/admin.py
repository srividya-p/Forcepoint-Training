from  doctor import Doctor
from login_system import LoginSystemInterface 

class Admin:
    def __init__(self, userName, authorizer = LoginSystemInterface):
        self.userName = userName
        self.authorizer = authorizer

    def createStaff(self):
        if not self.authorizer.isLoggedIn():
            print('You (Employee) are not logged in!')
            return

    def createDoctor(self, fullName, dob, gender, address, salary, funds, yearsOfExp, doctorType):
        if not self.authorizer.isLoggedIn():
            print('You are not logged in!')
            return

    def createReceptionist(self):
        if not self.authorizer.isLoggedIn():
            print('You are not logged in!')
            return

    def createPayroll(self):
        if not self.authorizer.isLoggedIn():
            print('You are not logged in!')
            return

    def createWard(self):
        if not self.authorizer.isLoggedIn():
            print('You are not logged in!')
            return