from uuid import uuid4
from login_system import LoginSystemInterface 

class User:
    def __init__(self, fullName, dob, gender, address, authorizer = LoginSystemInterface):
        self.uId = str(uuid4())
        self.dob = dob
        self.fullName = fullName
        self.gender = gender
        self.address = address
        self.authorizer = authorizer
        self.isExists = True