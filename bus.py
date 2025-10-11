class Vehicle:

    def __init__(self , name , max_speed , mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle): # THIS MEANS THAT THE CLASS HAS INHERITED ALL THE VARIABLES OF VEHICLE CLASS
    pass


School_bus = Bus("School Volvo" , 180 , 12)

print("Vehicle name is: ", School_bus.name , "Speed is: ", School_bus.max_speed , "Mileage is:", School_bus.mileage)
