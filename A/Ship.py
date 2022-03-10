from Vehicle import Vehicle

class Ship(Vehicle):

    age = 0
    type = ""
    country = ""

    #constructors
    def __init__(self, age = 0, type = "", country = ""):
        self.age = age
        self.type = type
        self.country = country

    #methods
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age
    
    def setType(self, type):
        self.type = type
    def getType(self):
        return self.type

    def setCountry(self, country):
        self.country = country
    def getCountry(self):
        return self.country

    def print(self):
        print("Ship's Name          : " + str(self.name))
        print("Ship's Age           : " + str(self.age) + " years")
        print("Ship's Type          : " + str(self.type))
        print("Manufactured in      : " + str(self.country)) 
        print("Fuel Type            : " + str(self.fuel))
        print("Maximum Passengers   : " + str(self.max_passengers))
        self.Move()