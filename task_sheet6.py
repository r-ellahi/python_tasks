# class Vehicle:
#     def __init__(self,
#                  max_speed: int,
#                  colour: str,
#                  ):
        
#         self.max_speed = max_speed
#         self.colour = colour

# vehicle_1 = Vehicle(70, 'blue')
# print(vehicle_1.max_speed, vehicle_1.colour)


# Q1 create a Vehicle class without any attributes and methods
class Vehicle():
    
    
#Q2 Extend the Vehicle class to contain attributes for max speed and colour
max_speed = 200
colour = ''
    

    #Q3 Extend Vehicle class to contain methods for max_speed and colour. 
    # Instantantiate the class and call the two methods ato update the attributes 
    # Print out the changes
def change_colour(self, new_colour):
    self.colour = new_colour
    
car = Vehicle()
print(car.colour)
car.change_colour("yellow")
print(car.colour)


# Q4 create a child class Bus that will inherit all variables and methods of thr Vehicle class
# Instantantiate the class and call the two methods ato update the attributes 





#Q1 - SAM
# class Bus(Vehicle):
#     pass

# #q2 - SAM
# class Bus(Vehicle):
#     def __init__(self, max_speed, colour):
#         self.max_speed = max_speed
#         self.colour = colour

# vehicle = Vehicle(150, 'colour')
# print(vehicle.max_speed, vehicle.colour)
        
        
 #q3 - SAM
class Bus(Vehicle):
    def __init__(self, max_speed, colour):
        self.max_speed = max_speed
        self.colour = colour    
    
    def update_max_speed(self, speed):
        self.max_speed += speed
        
    def update_colour(self, colour):
        self.colour = colour   
        
        
vehicle = Vehicle(150, 'colour')
print(vehicle.max_speed, vehicle.colour)

vehicle.update_max_speed(50)
vehicle.update_colour('blue')
print(vehicle.max_speed, vehicle.colour)
        
