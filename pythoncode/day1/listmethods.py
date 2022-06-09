my_fruit = ["Apple", "Bananas", "Orange"]

#list.append() append objects ot the end of a list
my_fruit.append("Watermelon")
print(my_fruit)

#list.remove() removes object from list
my_fruit.remove("apple")
print(my_fruit)
#If item exists twice it will only remove the 1st occurance

#list.pop() removes and returns items at index
varfruit = my_fruit.pop(-1)
print(my_fruit)
print(varfruit)

#list.insert() inserts an object before the index
my_fruit.insert(1, "Mega-fruit")
print(my_fruit)

#list.extend can extend a list by another list or any iterable variable
my_fruit2 = ["Strawberry", "Kiwi", "Mango"]
my_fruit.extend(my_fruit2)
print(my_fruit)

#list.index - returns the first index of the value
print(my_fruit.index("Strawberry"))

#list.count() returns the number of occurances of a value in a list
print(my_fruit.count("Strawberry"))

#list.sort() allows us to sort list in ascending order
my_fruit.sort()
print(my_fruit)