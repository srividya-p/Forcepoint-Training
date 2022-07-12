from contact import Contact
from contact_detail import ContactDetail

class User:
    userId = -1
    userList = []
    def __init__(self, userName, firstName, lastName, isActive, isAdmin, contacts):
        self.userId = User.userId
        self.userName = userName
        self.firstName, self.lastName = firstName, lastName
        self.isAdmin, self.isActive = isAdmin, isActive
        self.contacts = contacts

    def getContactIndex(self, contactName):
        firstName, lastName = contactName.split(' ')
        for i in range(len(self.contacts)):
            if self.contacts[i].firstName == firstName and self.contacts[i].lastName == lastName:
                return i

        return -1 

    def getDetailIndex(self, contactIndex, contactDetail):
        contactDetails = self.contacts[contactIndex].contactDetails
        for i in range(len(contactDetails)):
            if contactDetails[i].contactDetail == contactDetail:
                return i

        return -1 

    @staticmethod
    def findUserByName(userName):
        for user in User.userList:
            if user.userName == userName:
                return user
        return None

    def createUser(self, userName, firstName, lastName, isActive, contacts, isAdmin = False):
        if not self.isAdmin:
            print("You do not have the permission to create a user!")
            return
        
        User.userId += 1
        newUser = User(userName, firstName, lastName, isActive, isAdmin, contacts)
        User.userList.append(newUser)
        return newUser

    def readUser(self, userName):
        if not self.isAdmin:
            print("You do not have the permission to read a user!")
            return

        user = User.findUserByName(userName)
        if user is None:
            print("Username not found!")
            return

        print(user.userId, user.firstName, user.lastName, user.isActive, user.contacts)

    def updateUser(self, userName, propertyName, newValue):
        if not self.isAdmin:
            print("You do not have the permission to update a user!")
            return

        user = User.findUserByName(userName)
        if user is None:
            print("Username not found!")
            return

        if propertyName == 'contacts':
            pass
        else:
            oldValue = str(getattr(user, propertyName))
            setattr(user, propertyName, newValue)
            print(user.firstName+" "+user.lastName+"'s "+propertyName+" changed from "+oldValue
                    +" to "+str(getattr(user, propertyName)))

    def deleteUser(self, userName):
        if not self.isAdmin:
            print("You do not have the permission to delete a user!")
            return

        user = User.findUserByName(userName)
        if user is None:
            print("Username not found!")
            return

        user.isActive = False

    def createContact(self, firstName, lastName, isActive, contactDetails):
        if not self.isActive:
            print("You are not active! You cannot create a contact.")
            return
        
        newContact = Contact.createContact(firstName, lastName, isActive, contactDetails)
        self.contacts.append(newContact)

    def readContact(self, contactName):
        if not self.isActive:
            print("You are not active! You cannot read a contact.")
            return
        
        index = self.getContactIndex(contactName)
        if index == -1:
            print("This contact name does not exist!")
            return
        
        contact = self.contacts[index]
        print(contact.firstName, contact.lastName, contact.isActive, contact.contactDetails)
        
    def updateContact(self, contactName, propertyName, newValue):
        if not self.isActive:
            print("You are not active! You cannot update a contact.")
            return

        index = self.getContactIndex(contactName)
        if index == -1:
            print("This contact name does not exist!")
            return

        if propertyName == 'contactDetails':
            pass
        else:
            contact = self.contacts[index]
            oldValue = str(getattr(contact, propertyName))
            setattr(contact, propertyName, newValue)
            
            print(contact.firstName+" " + contact.lastName + "'s "+ propertyName + " changed from " 
            + oldValue + " to " + str(getattr(contact, propertyName)))

    def deleteContact(self, contactName):
        if not self.isActive:
            print("You are not active! You cannot delete a contact.")
            return

        index = self.getContactIndex(contactName)
        if index == -1:
            print("This contact name does not exist!")
            return

        self.contacts.pop(index)

    def createContactDetail(self, contactName, detailType, detail):
        if not self.isActive:
            print("You are not active! You cannot create a contact detail.")
            return
        
        index = self.getContactIndex(contactName)
        if index == -1:
            print("This contact name does not exist!")
            return

        contactDetail = ContactDetail.createContactDetail(detailType, detail)
        self.contacts[index].contactDetails.append(contactDetail)

    def readContactDetail(self, contactName, contactDetail):
        if not self.isActive:
            print("You are not active! You cannot read a contact.")
            return

        contactIndex = self.getContactIndex(contactName)
        if contactIndex == -1:
            print("This contact name does not exist!")
            return

        detailIndex = self.getDetailIndex(contactIndex, contactDetail)
        if detailIndex == -1:
            print("This detail does not exist!")
            return
        
        detail = self.contacts[contactIndex].contactDetails[detailIndex]
        print(detail.detailId, detail.detailType, detail.contactDetail)

    def updateContactDetail(self, contactName, contactDetail, propertyName, newValue):
        if not self.isActive:
            print("You are not active! You cannot update a contact detail.")
            return
        
        contactIndex = self.getContactIndex(contactName)
        if contactIndex == -1:
            print("This contact name does not exist!")
            return

        detailIndex = self.getDetailIndex(contactIndex, contactDetail)
        if detailIndex == -1:
            print("This detail does not exist!")
            return

        detail = self.contacts[contactIndex].contactDetails[detailIndex]
        oldValue = str(getattr(detail, propertyName))
        setattr(detail, propertyName, newValue)
        
        print("Detail ID " + str(detail.detailId) + "'s "+ propertyName + " changed from " 
        + oldValue + " to " + str(getattr(detail, propertyName)))

    def deleteContactDetail(self, contactName, contactDetail):
        if not self.isActive:
            print("You are not active! You cannot delete a contact detail.")
            return

        contactIndex = self.getContactIndex(contactName)
        if contactIndex == -1:
            print("This contact name does not exist!")
            return

        detailIndex = self.getDetailIndex(contactIndex, contactDetail)
        if detailIndex == -1:
            print("This detail does not exist!")
            return

        self.contacts[contactIndex].contactDetails.pop(detailIndex)