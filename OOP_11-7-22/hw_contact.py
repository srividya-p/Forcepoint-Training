class ContactDetail:
    def __init__(self, detailId, detailType, contactDetail):
        self.detailId = detailId
        self.detailType, self.contactDetail = detailType, contactDetail

class Contact:
    def __init__(self, contactId, firstName, lastName, isActive, contactDetails):
        self.contactId = contactId
        self.firstName, self.lastName = firstName, lastName
        self.isActive = isActive
        self.contactDetails = contactDetails

class User:
    def __init__(self, userId, firstName, lastName, isActive, isAdmin, contacts):
        self.userId = userId
        self.firstName, self.lastName = firstName, lastName
        self.isAdmin, self.isActive = isAdmin, isActive
        self.contacts = contacts

    def createUser(self, userId, firstName, lastName, isActive, contacts, isAdmin = False):
        if not self.isAdmin:
            print("You do not have the permission to create a user!")
            return
        
        return User(userId, firstName, lastName, isActive, isAdmin, contacts)

    def readUser(self, user):
        if not self.isAdmin:
            print("You do not have the permission to read a user!")
            return

        print(user.userId, user.firstName, user.lastName, user.isActive, user.contacts)

    def updateUser(self, user, propertyName, newValue):
        if not self.isAdmin:
            print("You do not have the permission to update a user!")
            return

        if propertyName == 'contacts':
            pass
        else:
            oldValue = str(getattr(user, propertyName))
            setattr(user, propertyName, newValue)
            print(user.firstName+" "+user.lastName+"'s "+propertyName+" changed from "+oldValue
                    +" to "+str(getattr(user, propertyName)))

    def deleteUser(self, user):
        if not self.isAdmin:
            print("You do not have the permission to delete a user!")
            return

        user.isActive = False

    def createContact(self, contact):
        if not self.isActive:
            print("You are not active! You cannot create a contact.")
            return
        
        self.contacts.append(contact)

    def readContact(self, index):
        if not self.isActive:
            print("You are not active! You cannot read a contact.")
            return
        contact = self.contacts[index]
        print(contact.firstName, contact.lastName, contact.isActive, contact.contactDetails)
        

    def updateContact(self, index, propertyName, newValue):
        if not self.isActive:
            print("You are not active! You cannot update a contact.")
            return

        if propertyName == 'contactDetails':
            pass
        else:
            contact = self.contacts[index]
            oldValue = str(getattr(contact, propertyName))
            setattr(contact, propertyName, newValue)
            
            print(contact.firstName+" " + contact.lastName + "'s "+ propertyName + " changed from " 
            + oldValue + " to " + str(getattr(contact, propertyName)))

    def deleteContact(self, index):
        if not self.isActive:
            print("You are not active! You cannot delete a contact.")
            return

        self.contacts.pop(index)

    def createContactDetail(self, index, contactDetail):
        if not self.isActive:
            print("You are not active! You cannot create a contact detail.")
            return
        
        self.contacts[index].contactDetails.append(contactDetail)

    def readContactDetail(self, contactIndex, detailIndex):
        if not self.isActive:
            print("You are not active! You cannot read a contact.")
            return
        detail = self.contacts[contactIndex].contactDetails[detailIndex]
        print(detail.detailId, detail.detailType, detail.contactDetail)

    def updateContactDetail(self, contactIndex, detailIndex, propertyName, newValue):
        if not self.isActive:
            print("You are not active! You cannot update a contact detail.")
            return
        
        detail = self.contacts[contactIndex].contactDetails[detailIndex]
        oldValue = str(getattr(detail, propertyName))
        setattr(detail, propertyName, newValue)
        
        print("Detail ID " + str(detail.detailId) + "'s "+ propertyName + " changed from " 
        + oldValue + " to " + str(getattr(detail, propertyName)))

    def deleteContactDetail(self, contactIndex, detailIndex):
        if not self.isActive:
            print("You are not active! You cannot delete a contact detail.")
            return

        self.contacts[contactIndex].contactDetails.pop(detailIndex)

try:
    admin = User(0, "Admin", "A", True, True, [])

    print('---------- USER CRUD -----------')
    user1 = admin.createUser(1, "User", "B", True, [])
    user2 = admin.createUser(2, "User", "C", True, [])
    user3 = admin.createUser(3, "User", "D", True, [])

    user4 = user3.createUser(4, "User", "E", True, []) # Permission check
    admin.readUser(user1)
    admin.updateUser(user1, 'userId', 11)
    print('Deleting user1.')
    admin.deleteUser(user1)
    admin.readUser(user1)

    print('\n---------- CONTACT CRUD ---------')
    user2.createContact(Contact(11, 'Contact', 'A', True, []))
    user2.createContact(Contact(12, 'Contact', 'B', False, []))
    user3.createContact(Contact(13, 'Contact', 'C', False, []))
    user3.createContact(Contact(14, 'Contact', 'D', True, []))
    user3.createContact(Contact(15, 'Contact', 'E', False, []))

    user1.readContact(0) # Inactive check
    user2.readContact(0)
    user3.readContact(1)
    user3.updateContact(0, 'isActive', True)
    print('Deleting Contact E of user3.')
    user3.deleteContact(2)
    # user3.readContact(2)

    print('\n------ CONTACT DETAIL CRUD ------')
    user2.createContactDetail(0, ContactDetail(100, 'email', 'abc@gmail.com'))
    user2.createContactDetail(0, ContactDetail(102, 'work', '022-3779-6690'))
    user2.createContactDetail(1, ContactDetail(106, 'personal', '+91-9870234498'))
    user3.createContactDetail(0, ContactDetail(103, 'personal', '+91-9877635488'))
    user3.createContactDetail(1, ContactDetail(104, 'landline', '022-3423-8867'))
    user3.createContactDetail(1, ContactDetail(105, 'email', 'def@gmail.com'))

    user2.readContactDetail(0, 0)
    user3.readContactDetail(1, 0)
    user2.updateContactDetail(0, 1, 'detailType', 'landline')
    print('Deleting Contact Detail 105 of user3.')
    user3.deleteContactDetail(1, 1)
    user3.readContactDetail(1, 1)

except AttributeError:
    print('This property does not exist!')

except IndexError:
    print('This index does not exist!')