#Qn 1- created  a class called vehicle
class Vehicle:
    def __init__(self,max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# Qn2-created an object Bus inheriting the class
#my class 
class Vehicle:
    def __init__(self,name,max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
#my object inheriting from the class
Bus = Vehicle("School Volvo", 180, "12")
print("Name: {} Speed: {} Mileage: {}".format(Bus.name, Bus.max_speed, Bus.mileage))

#Qn 3- created a Bus class inheriting from vehicle
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, seating_capacity=50):
        super().__init__(name,max_speed, mileage)
        self.seating_capacity = seating_capacity
coaches = Bus("School Volvo", "180", "12", "50")
print("The seating capacity of a bus is", coaches.seating_capacity, "passengers")

#Qn 4 - 
class Vehicle:
    color = "white"
    def __init__(self,name,max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass
class Car(Vehicle):
    pass
motor1 = Bus("School Volvo", "180", "12")
print("Color:", motor1.color, "," "Vehicle name:", motor1.name,"," "Speed:", motor1.max_speed,"," "Mileage:", motor1.mileage)
motor2 = Car("Audi Q5", "240", "18")
print("Color:", motor2.color, ",", "Vehicle name:", motor2.name,"," "Speed:", motor2.max_speed,"," "Mileage:", motor2.mileage)

#Qn 5
class Vehicle:
    def __init__(self,name,mileage,capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100
class Bus(Vehicle):
    def fare(self):
        amount = self.capacity * 100
        return amount + 0.1*amount #amount is my variable
        
School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
