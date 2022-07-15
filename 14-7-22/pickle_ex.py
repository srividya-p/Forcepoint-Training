import pickle

class Person:
    def __init__(self, name, age) -> None:
        self.name, self.age = name, age

    def increaseAge(self, years):
        self.age += years

    def getPersonDetails(self):
        return f"{self.name} is {self.age} years old."

if __name__ == '__main__':
    me = Person('Srividya', 12)
    people = [Person('Srividya', 12), Person('Archit', 13), Person('Sara', 14)]

    #Not stored as an object key value pair.
    #file = open('persons.txt', 'w')
    #file.write(me.getPersonDetails())

    dumpStr = pickle.dumps(people)
    print(dumpStr)
    loadStr = pickle.loads(dumpStr)
    print(loadStr)

    file = open('persons.pickle', 'wb')
    pickle.dump(people, file)
    file.close()

    file = open('persons.pickle', 'rb')
    data = pickle.load(file)
    for person in data:
        print(person.getPersonDetails())

