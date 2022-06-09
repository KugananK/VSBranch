my_words = {"Hello":"Hola", "Thank you":"Gracias", "Yes":"Si"}

for key in my_words:
    print(key)
#returns
#Hello
#Thank you
#Yes

#to get values
for value in my_words.values():
    print(value)
#returns
#Hola
#Gracias
#Si

for keyvalue in my_words.items():
    print(keyvalue)
#returns
#('Hello', 'Hola')
#('Thank you', 'Gracias')
#('Yes', 'Si')