class Person():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __move(self):
        print("walk")

class Student():
    def __init__(self, person, rollno):
        self.person = person
        self.rollno = rollno

    def eat(self):
        print("pizza")

s = Student(Person("A", 1), 11)

s.person.__move()