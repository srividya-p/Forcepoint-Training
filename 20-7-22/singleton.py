admin = None

class Admin:
    def __init__(self, name, age) -> None:
        self.name, self.age = name, age

    @staticmethod
    def createAdmin(name, age):
        if admin != None: return admin
        return Admin('admin', 50)

admin = Admin.createAdmin()
me = Admin.createAdmin()