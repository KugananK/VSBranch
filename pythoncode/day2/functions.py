#Functions are procedures that will run all its code to the end
#not returning any value which can be used elsewhere.
#a function will return a value which can be used later on

#uses for return value
    #Store in variable
    #use in calculation
    #Use as a parameter in another function/procedure

usergreeting = input("Enter a greeting")
username = input("Enter your name")

def shout(greeting, name):
    gup = str(greeting).upper()
    nup = str(name).upper()
    return f'{gup} {nup}'

print(shout(usergreeting, username))

#Setup the same as a procedure but has the return value which can be used later
#username and usergreeting are variables that can be passed into functions

#We can provide our function/procedure with default values by putting
# = by the parameter name

def greet(name="Ryan"):
    return f'hello {name}'

print(greet())
#prints out hello ryan as this is the default value assigned without input
