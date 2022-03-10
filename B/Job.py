from tkinter import W


class Job():

    worker_id = ""
    company = ""
    occupation = ""

    #constructor
    def __init__(self, worker_id = "", company = "", occupation = ""):
        self.worker_id = worker_id
        self.company = company
        self.occupation = occupation

    #methods
    def setW_ID(self, worker_id):
        self.worker_id = worker_id
    def getW_ID(self):
        return self.worker_id

    def setCompany(self, company):
        self.company = company
    def getCompany(self):
        return self.company

    def setOccupation(self, occupation):
        self.occupation = occupation
    def getOccupation(self):
        return self.occupation
    
    def print_Job(self):
        print("Company Name     : " + str(self.company))
        print("Worker ID        : " + str(self.worker_id))
        print("Position         : " + str(self.occupation))