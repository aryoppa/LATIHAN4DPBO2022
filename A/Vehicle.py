class Vehicle():

    name = ""
    fuel = ""
    max_passengers = 0

    #constructor
    def __init__(self, name = "", fuel = "", max_passengers = 0):
        self.name = name
        self.fuel = fuel
        self.max_passengers = max_passengers

    #methods
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setFuel(self, fuel):
        self.fuel = fuel
    def getFuel(self):
        return self.fuel
    
    def setPassengers(self, x):
        self.max_passengers = x
    def getPassengers(self):
        return self.max_passengers

    def Move(self):
        print(self.name + " is moving...")

    def print(self):
        print("Vehicle's Name       : " + str(self.name))
        print("Fuel Type            : " + str(self.fuel))
        print("Maximum Passengers   : " + str(self.max_passengers))
        self.Move()