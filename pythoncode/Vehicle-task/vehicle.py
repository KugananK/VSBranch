class Vehicle:
    def __init__(self, max_speed = '0', mileage = '0'):
        self.max_speed = max_speed
        self.mileage = mileage

vehicle1 = Vehicle()
print(vehicle1.__dict__)

class Bus(Vehicle):
    def __init__(self, max_speed, mileage)
        super().__init__(self, max_speed, mileage)

bus1 = Bus(100, 1200)

class Bus2(Vehicle):
    def __init__(self, max_speed, mileage, seats = 50)
        super().__init__(self, max_speed, mileage)
        self.seats = seats

bus2 = Bus(200, 2400)