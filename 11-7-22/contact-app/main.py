from user import User

try:
    admin = User(0, "Admin", "A", True, True, [])

    print('---------- USER CRUD -----------')
    user1 = admin.createUser('b', "User", "B", True, [])
    user2 = admin.createUser('c', "User", "C", True, [])
    user3 = admin.createUser('d', "User", "D", True, [])

    user4 = user3.createUser('e', "User", "E", True, []) # Permission check
    admin.readUser('b')
    admin.updateUser('b', 'userId', 11)
    print('Deleting User B.')
    admin.deleteUser('b')
    admin.readUser('b')

    print('\n---------- CONTACT CRUD ---------')
    user2.createContact('Contact', 'A', True, [])
    user2.createContact('Contact', 'B', False, [])
    user3.createContact('Contact', 'C', False, [])
    user3.createContact('Contact', 'D', True, [])
    user3.createContact('Contact', 'E', False, [])

    user1.readContact('Contact A') # Inactive check
    user2.readContact('Contact A')
    user3.readContact('Contact D')
    user3.updateContact('Contact C', 'isActive', True)
    print('Deleting Contact E of user3.')
    user3.deleteContact('Contact E')
    user3.readContact('Contact E')

    print('\n------ CONTACT DETAIL CRUD ------')
    user2.createContactDetail('Contact A', 'email', 'abc@gmail.com')
    user2.createContactDetail('Contact A', 'work', '022-3779-6690')
    user2.createContactDetail('Contact B', 'personal', '+91-9870234498')
    user3.createContactDetail('Contact C', 'personal', '+91-9877635488')
    user3.createContactDetail('Contact D', 'landline', '022-3423-8867')
    user3.createContactDetail('Contact D', 'email', 'def@gmail.com')

    user2.readContactDetail('Contact A', 'abc@gmail.com')
    user3.readContactDetail('Contact D', '022-3423-8867')
    user2.updateContactDetail('Contact A', '022-3779-6690', 'detailType', 'landline')
    print('Deleting Contact Detail def@gmail.com of user3.')
    user3.deleteContactDetail('Contact D', 'def@gmail.com')
    user3.readContactDetail('Contact D', 'def@gmail.com')

except AttributeError:
    print('This property does not exist!')

except IndexError:
    print('This index does not exist!')