noises = {"Cow":"Moo", "Sheep":"Baaa", "Owen Wilson":"Wow"}
print(noises["Owen Wilson"])

#How to add to dictionary
noises["Car"] = "Vroom"
print(noises)

#How to overwrite values in dictionary
noises["Sheep"] = "BAAh"

#How to return keys in dictionary
print(list(noises.keys()))

#how to return values in dictionary
print(list(noises.Values()))

#how to return dictionary as list contating typles of key value pairs
print(list(noises.items()))
print("Moo" in noises)
#Returns false as moo is not in keys
print("Moo" in noises.values())
#Returns True

my_words = {"Hello":"Hola", "Thank you":"Gracias"}
#get is used to return value if key is in dictionary
print(my_words.get("Hello"))

#pop can remove specified key and return value
grac = my_words.pop("Thank you")
print(grac)
print(my_words)

#update can add to or list or update values
my_words.update({"Yes":"Ci"})
print(my_words)
my_words.update({"Yes":"Si"})
print(my_words)
