#class example
#class seems to be like java super class?


class Dog: #We define class with class keyword, needs to start with capital
    leg_count = 4 #default attributes
    breed = "Springer"
    fur_colour = "Blue"
    def speak(self):
        print("Woof")

bilbo_wagins = dog() #creating objects of the class
betsy = dog()
fido = dog()

bilbo_wagins.speak() #calling methods from class instances

bilbo_wagins.breed = "German Sheppard" #changing class attributes
print(bilbo_wagins.breed)

attributes = dir(bilbo_wagins)
print(attributes) #printing out all attributes