my_words = {"Hello":"Hola", "Thank you":"Gracias", "Yes":"Si"}
result = []

for x in my_words:
    result.append(x)
    print(result)

for x in my_words.values():
    result.append(x)
    print(result)

#returns
# ['Hello']
# ['Hello', 'Thank you']
# ['Hello', 'Thank you', 'Yes']
# ['Hello', 'Thank you', 'Yes', 'Hola']
# ['Hello', 'Thank you', 'Yes', 'Hola', 'Gracias']
# ['Hello', 'Thank you', 'Yes', 'Hola', 'Gracias', 'Si']