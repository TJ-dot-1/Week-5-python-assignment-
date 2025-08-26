from abc import ABC, abstractmethod
from datetime import datetime
import random

# Abstract base class using abstraction
class Vehicle(ABC):
    def __init__(self, name, max_speed, fuel_type):
        self.name = name
        self.max_speed = max_speed
        self.fuel_type = fuel_type
        self.current_speed = 0
        self.is_moving = False
        self.creation_date = datetime.now()
    
    @abstractmethod
    def move(self):
        pass
    
    def start(self):
        if not self.is_moving:
            self.is_moving = True
            self.current_speed = 10
            print(f"🚀 {self.name} has started!")
        else:
            print(f"⚠️  {self.name} is already moving!")
    
    def stop(self):
        if self.is_moving:
            self.is_moving = False
            self.current_speed = 0
            print(f"🛑 {self.name} has stopped!")
        else:
            print(f"⚠️  {self.name} is already stopped!")
    
    def accelerate(self, amount):
        if self.is_moving:
            self.current_speed = min(self.max_speed, self.current_speed + amount)
            print(f"⚡ {self.name} accelerated to {self.current_speed} km/h!")
        else:
            print(f"⚠️  Start {self.name} first!")
    
    def get_age(self):
        age = datetime.now() - self.creation_date
        return f"{age.days} days old"
    
    def __str__(self):
        return f"{self.name} ({self.fuel_type}, max: {self.max_speed}km/h)"


# Car class - moves by driving
class Car(Vehicle):
    def __init__(self, name, max_speed, fuel_type, doors):
        super().__init__(name, max_speed, fuel_type)
        self.doors = doors
        self.gear = "P"  # Park
    
    def move(self):
        if not self.is_moving:
            self.start()
        print(f"🚗 {self.name} is driving on the road at {self.current_speed} km/h!")
        return "Driving"
    
    def change_gear(self, new_gear):
        gears = ["P", "R", "N", "D", "1", "2", "3", "4", "5", "6"]
        if new_gear in gears:
            self.gear = new_gear
            print(f"🔧 {self.name} shifted to gear {new_gear}")
        else:
            print("❌ Invalid gear!")


# Plane class - moves by flying
class Plane(Vehicle):
    def __init__(self, name, max_speed, fuel_type, wingspan):
        super().__init__(name, max_speed, fuel_type)
        self.wingspan = wingspan
        self.altitude = 0
        self.is_flying = False
    
    def move(self):
        if not self.is_moving:
            self.take_off()
        print(f"✈️  {self.name} is flying at {self.altitude}m altitude, speed: {self.current_speed} km/h!")
        return "Flying"
    
    def take_off(self):
        if not self.is_flying:
            self.is_moving = True
            self.is_flying = True
            self.current_speed = 200
            self.altitude = 1000
            print(f"🛫 {self.name} has taken off!")
    
    def land(self):
        if self.is_flying:
            self.is_moving = False
            self.is_flying = False
            self.current_speed = 0
            self.altitude = 0
            print(f"🛬 {self.name} has landed!")
        else:
            print(f"⚠️  {self.name} is not flying!")


# Boat class - moves by sailing
class Boat(Vehicle):
    def __init__(self, name, max_speed, fuel_type, displacement):
        super().__init__(name, max_speed, fuel_type)
        self.displacement = displacement
        self.anchor_down = True
    
    def move(self):
        if not self.is_moving:
            self.raise_anchor()
        print(f"⛵ {self.name} is sailing on water at {self.current_speed} km/h!")
        return "Sailing"
    
    def raise_anchor(self):
        if self.anchor_down:
            self.anchor_down = False
            self.is_moving = True
            self.current_speed = 15
            print(f"⚓ Anchor raised! {self.name} is ready to sail!")
    
    def drop_anchor(self):
        if not self.anchor_down:
            self.anchor_down = True
            self.is_moving = False
            self.current_speed = 0
            print(f"⚓ Anchor dropped! {self.name} is stationary.")


# Bicycle class - moves by pedaling (no fuel!)
class Bicycle(Vehicle):
    def __init__(self, name, max_speed, gears):
        super().__init__(name, max_speed, "Human Power")
        self.gears = gears
        self.current_gear = 1
    
    def move(self):
        if not self.is_moving:
            self.start()
        print(f"🚴 {self.name} is pedaling at gear {self.current_gear}, speed: {self.current_speed} km/h!")
        return "Pedaling"
    
    def shift_gear(self, gear):
        if 1 <= gear <= self.gears:
            self.current_gear = gear
            print(f"🔧 {self.name} shifted to gear {gear}")
        else:
            print(f"❌ {self.name} only has {self.gears} gears!")


# Motorcycle class - moves by riding
class Motorcycle(Vehicle):
    def __init__(self, name, max_speed, fuel_type, engine_size):
        super().__init__(name, max_speed, fuel_type)
        self.engine_size = engine_size
        self.helmet_on = False
    
    def move(self):
        if not self.is_moving:
            self.start()
        safety = "with helmet ✅" if self.helmet_on else "NO helmet ❌"
        print(f"🏍️  {self.name} is riding {safety} at {self.current_speed} km/h!")
        return "Riding"
    
    def wear_helmet(self):
        self.helmet_on = True
        print(f"🪖 Helmet on! {self.name} is safe to ride!")
    
    def remove_helmet(self):
        self.helmet_on = False
        print(f"⚠️  Helmet removed! Ride carefully!")


# Demonstration function
def vehicle_showcase():
    print("=== VEHICLE MOVEMENT DEMO ===\n")
    
    # Create different vehicles
    vehicles = [
        Car("Toyota Camry", 180, "Gasoline", 4),
        Plane("Boeing 747", 920, "Jet Fuel", 64.4),
        Boat("Sailboat Explorer", 25, "Wind", 1500),
        Bicycle("Mountain Bike", 40, 21),
        Motorcycle("Harley Davidson", 180, "Gasoline", 1200)
    ]
    
    # Demonstrate polymorphism - same method, different behavior
    for vehicle in vehicles:
        print(f"\n{'='*50}")
        print(f"Testing: {vehicle}")
        print(f"Age: {vehicle.get_age()}")
        
        # Each vehicle moves differently!
        movement_type = vehicle.move()
        print(f"Movement type: {movement_type}")
        
        # Accelerate a bit
        vehicle.accelerate(random.randint(20, 50))
        vehicle.move()
        
        # Stop the vehicle
        if isinstance(vehicle, Plane):
            vehicle.land()
        elif isinstance(vehicle, Boat):
            vehicle.drop_anchor()
        else:
            vehicle.stop()
        
        # Show some unique features
        if isinstance(vehicle, Car):
            vehicle.change_gear("D")
        elif isinstance(vehicle, Bicycle):
            vehicle.shift_gear(3)
        elif isinstance(vehicle, Motorcycle):
            vehicle.wear_helmet()

    print(f"\n{'='*50}")
    print("🎉 All vehicles demonstrated their unique movement styles!")


# Run the demonstration
if __name__ == "__main__":
    vehicle_showcase()
    
    # Additional interactive demo
    print("\n\n=== INTERACTIVE DEMO ===")
    my_car = Car("Honda Civic", 200, "Gasoline", 4)
    my_plane = Plane("Airbus A320", 890, "Jet Fuel", 35.8)
    
    # Show how they both have move() but behave differently
    print("\nLet's compare movement:")
    print(f"Car movement: {my_car.move()}")
    print(f"Plane movement: {my_plane.move()}")
    
    # Demonstrate they're both Vehicles (polymorphism)
    transport_list = [my_car, my_plane]
    for transport in transport_list:
        print(f"\n{transport.name} says: ", end="")
        transport.move()