from uuid import uuid4

class User:
    def __init__(self, userName, password, fullName, dob, age, gender, address, isAdmin) -> None:
        self.uId = str(uuid4())
        self.userName, self.password = userName, password
        self.dob, self.age = dob, age
        self.fullName = fullName
        self.gender, self.address = gender, address
        self.isLoggedIn = False
        self.isAdmin = isAdmin

    def login(self, username, password):
        #check credentials
        self.isLoggedIn = True

    def logout():
        pass