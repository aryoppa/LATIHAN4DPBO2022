
from Person import Person
from Job import Job
from Driver import Driver

#dummy data for Persons
print("=====================")
p1 = Person()
p1.setName("Aryo")
p1.setID("12345678")
p1.setGender("Male")
p1.print_Person()
print("")
p1.Sleep()

p2 = Person()
p2.setName("Gatot Kaca")
p2.setID("87654321")
p2.setGender("Male")
print("")
p2.print_Person()
p2.Sleep()

p3 = Person()
p3.setName("Mike Wazowsky")
p3.setID("18273645")
p3.setGender("Male")
print("")
p3.print_Person()
p3.Sleep()

p4 = Person()
p4.setName("Yayang")
p4.setID("45362718")
p4.setGender("Female")
print("")
p4.print_Person()
p4.Sleep()

p5 = Person()
p5.setName("Angelina Jolie")
p5.setID("81726354")
p5.setGender("Female")
print("")
p5.print_Person()
p5.Sleep()

#dummy data for Jobs
print("")
print("=====================")
j1 = Job()
j1.setCompany("Muara Buana")
j1.setW_ID("A1B2C3")
j1.setOccupation("Manager")
print("")
j1.print_Job()

j2 = Job()
j2.setCompany("Tirta Kencana")
j2.setW_ID("1A2B3C")
j2.setOccupation("IT Consultant")
print("")
j2.print_Job()

j3 = Job()
j3.setCompany("Perantara")
j3.setW_ID("ABC123")
j3.setOccupation("CEO")
print("")
j3.print_Job()

j4 = Job()
j4.setCompany("Tampomas Coffee")
j4.setW_ID("123ABC")
j4.setOccupation("Co-Founder")
print("")
j4.print_Job()

j5 = Job()
j5.setCompany("Ensiklopi")
j5.setW_ID("AABBCC")
j5.setOccupation("Co-Founder & CEO")
print("")
j5.print_Job()

# dummy data for Drivers
# for Drivers, we must set the Occupation on job Object as Driver
print("")
print("=====================")
d1 = Driver("YDY", "02 Mar, 2045", "Ship", p1, j1)
j1.setOccupation("Driver")
print("")
d1.print_Driver()

d2 = Driver("321", "08 April, 2033", "Motorcycle", p2, j2)
j2.setOccupation("Driver")
print("")
d2.print_Driver()

d3 = Driver("ABC", "08 August, 2053", "Plane", p3, j3)
j3.setOccupation("Driver")
print("")
d3.print_Driver()

d4 = Driver("ABP", "14 February, 2035", "Ship", p4, j4)
j4.setOccupation("Driver")
print("")
d4.print_Driver()

d5 = Driver("A2C", "21 October, 2014", "Truck", p5, j5)
j5.setOccupation("Driver")
print("")
d5.print_Driver()
print("=====================")