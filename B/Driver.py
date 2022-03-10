from Person import Person
from Job import Job

class Driver(Person, Job):

    Pobj = Person()
    Jobj = Job()
    license_id = ""
    exp_date = ""
    vehicle_type = ""

    #constructor
    def __init__(self, license_id = "", exp_date = "", vehicle_type = "", p = Person, j = Job):
        self.Pobj = p
        self.Jobj = j
        self.license_id = license_id
        self.exp_date = exp_date
        self.vehicle_type = vehicle_type

    #methods
    # def setPerson(self, p):
    #     self.p = p
    # def getPerson(self):
    #     return self.p

    # def setJob(self, j):
    #     self.Jobj = j

    def setLicense(self, license_id):
        self.license_id = license_id
    def getLicense(self):
        return self.license_id

    def setExp_date(self, exp_date):
        self.exp_date = exp_date
    def getExp_date(self):
        return self.exp_date

    def setVehicle(self, vehicle_type):
        self.vehicle_type = vehicle_type
    def getVehicle(self):
        return self.vehicle_type
    
    def print_Driver(self):
        print("Name             : " + str(self.Pobj.getName()))
        print("ID Number        : " + str(self.Pobj.getID()))
        print("Sex              : " + str(self.Pobj.getGender()))
        
        print("Company Name     : " + str(self.Jobj.getCompany()))
        print("Worker ID        : " + str(self.Jobj.getW_ID()))
        print("Position         : " + str(self.Jobj.getOccupation()))

        print("License ID       : " + str(self.license_id))
        print("Expired Date     : " + str(self.exp_date))
        print("Vehicle Type     : " + str(self.vehicle_type))