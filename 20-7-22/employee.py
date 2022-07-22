import json

class Employee:
    def __init__(self, name, designation, age) -> None:
        self.name = name
        self.designation = designation
        self.age = age
        self.subordinates = []

    def addSubordinate(self, name, designation, age):
        subordinate = Employee(name, designation, age)
        self.subordinates.append(subordinate)
        return subordinate

    def getTree(self, level = 0):
        ret = "\t"*level + self.name + ' - ' + self.designation + "\n"
        for subordinate in self.subordinates:
            ret += subordinate.getTree(level + 1)
        return ret

david = Employee('David Wallace', 'CFO', 50)

jan = david.addSubordinate('Jan Levison', 'VP', 30)
ryan = david.addSubordinate('Ryan Howard', 'VP', 30)

nellie = jan.addSubordinate('Nellie Burtram', 'Regional Manager', 30)
phyllis = nellie.addSubordinate('Phyllis Lapin', 'Salesman', 50)
stanley = nellie.addSubordinate('Stanley Hudson', 'Salesman', 50)

andy = jan.addSubordinate('Andy Bernard', 'Regional Manger', 20)
angela = andy.addSubordinate('Angela Martin', 'Accountant', 30)

michael = ryan.addSubordinate('Michael Scott', 'Regional Manager', 40)

dwight = michael.addSubordinate('Dwight Shrute', 'Asst. to RM', 40)
jim = michael.addSubordinate('Jim Halpert', 'Asst. to RM', 30)

print(david.getTree())

print('\n AS JSON \n')
data = json.dumps(david, default=lambda o: o.__dict__, indent = 4)
print(data)

