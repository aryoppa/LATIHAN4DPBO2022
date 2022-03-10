from Vehicle import Vehicle

class Airplane(Vehicle):

    age = 0
    type = ""
    wingspan = ""

    #constructors
    def __init__(self, age = 0, type = "", wingspan = ""):
        self.age = age
        self.type = type
        self.wingspan = wingspan

    #methods
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age
    
    def setType(self, type):
        self.type = type
    def getType(self):
        return self.type

    def setWingspan(self, wingspan):
        self.wingspan = wingspan
    def getWingspan(self):
        return self.wingspan

    def print(self):
        print("Plane's Name         : " + str(self.name))
        print("Plane's Age          : " + str(self.age) + " years")
        print("Plane's Type         : " + str(self.type))
        print("Wings Length         : " + str(self.wingspan)) 
        print("Fuel Type            : " + str(self.fuel))
        print("Maximum Passengers   : " + str(self.max_passengers))
        self.Move()