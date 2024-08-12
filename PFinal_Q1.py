import random

class Vehicle:
    def __init__(self, pilot_name, max_speed, color):
        self.pilot_name = pilot_name
        self.max_speed = max_speed
        self.color = color
        self.is_broken = False
        self.distance = 0
    
    def move(self):
        if not self.is_broken:
            speed = random.randint(0, self.max_speed)
            self.distance += speed / 50
    
    def crash(self):
        if random.randint(1, 1000) == 555:
            self.is_broken = True

class Race:
    def __init__(self, vehicles):
        self.vehicles = vehicles
    
    def start(self):
        while True:
            for vehicle in self.vehicles:
                vehicle.move()
                vehicle.crash()
                if vehicle.distance >= 100:
                    return self.get_winner()
            if all(vehicle.is_broken for vehicle in self.vehicles):
                return "All vehicles are crashed,therefore there is no winner."
    
    def get_winner(self):
        for vehicle in self.vehicles:
            if vehicle.distance >= 100:
                return f"The winner is {vehicle.pilot_name}!"
            
vehicles = [
    Vehicle("Meet", 80, "Black"),
    Vehicle("Jaydeep", 70, "Red"),
    Vehicle("Rutvik", 90, "Green"),
    Vehicle("Dev", 85, "Yellow"),
    Vehicle("Dhruv", 75, "Purple")
]
race = Race(vehicles)

for i in range(3):
    print(f"\nRace {i+1}:")
    print(race.start())
