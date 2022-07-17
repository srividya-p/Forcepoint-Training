from uuid import uuid4

class User:
    allUsers = []
    def __init__(self, userName, password, fullName, dob, age, gender, address, isAdmin):
        self.uId = str(uuid4())
        self.userName, self.password = userName, password
        self.dob, self.age = dob, age
        self.fullName = fullName
        self.gender, self.address = gender, address
        self.isLoggedIn = False
        self.isAdmin = isAdmin

    @staticmethod
    def createUser(userName, password, fullName, dob, age, gender, address):
        """Admin uses this method to create a user"""
        newUser = User(userName, password, fullName, dob, age, gender, address, True)
        User.allUsers.append(newUser)
        return newUser

    def readUser(self, userName):
        """Admin uses this method to read a user"""
        pass

    def editUser(self, username, property, newValue):
        """Admin uses this method to edit a user"""
        pass

    def deleteUser(self, username):
        """Admin uses this method to delete a user"""
        pass

    def login(self, username, password):
        """Login method for all actors"""
        self.isLoggedIn = True

    def logout():
        """Logout method for all actors"""
        pass