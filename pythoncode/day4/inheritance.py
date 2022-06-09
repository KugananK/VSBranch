class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal): #When defining a child class we put the name of the parent class in parentesis
    def __init__(self, name, fur_colour):
        super().__init__(name) #Super will call methods from parent class
        self.fur_colour = fur_colour

cat1 = Cat("Mittens", "Grey")

print(cat1.fur_colour)