class Person():

    id = ""
    name = ""
    gender = ""

    #construtor
    def __init__(self, id = "", name = "", gender = ""):
        self.id = id
        self.name = name
        self.gender = gender

    #methods
    def setID(self, id):
        self.id = id
    def getID(self):
        return self.id

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    
    def setGender(self, gender):
        self.gender = gender
    def getGender(self):
        return self.gender
    
    def Sleep(self):
        print(str(self.name) + " is sleeping...")

    def print_Person(self):
        print("Name             : " + str(self.name))
        print("ID Number        : " + str(self.id))
        print("Sex              : " + str(self.gender))