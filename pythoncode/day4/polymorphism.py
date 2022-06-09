class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speak")

class Cat(Animal):
    def __init__(self, name, fur_colour):
        super().__init__(name)
        self.fur_colour = fur_colour
    
    def speak(self):
        print("Meow")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        print("Woof")

dog1 = Dog("ivy", "IVY")
cat1 = Cat("Dotty", "3leg")

dog1.speak()
cat1.speak()