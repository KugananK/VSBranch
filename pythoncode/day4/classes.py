class Dog: create
    def __init__(self, name, breed, leg_count):
        #^This will run everytime a class is created
        self.name = name
        self.breed = breed
        self.leg_count = leg_count

dog1 = Dog("Jeff", "Pug", 4) # now we need to pass parameters into class construvtor

print(dog1.breed)