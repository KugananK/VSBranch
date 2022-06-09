list1 = ["Ryan", "Reece", "Adam", "Christopher"]

#We can reference the list element by putting the index in [] after the variable name
print(list1[1])
#we can reference the last element of the list by using [-1]
print(list1[-1])
#We can slice the list into smaller sections by using [x:y] after the variable name x= staring index, y= stopping index
print(list1[1:3])
#if we do not include the stopping point it will return all the values from the starting point)
print(list1[1:])

#we can changle the element in a list by setting a new value to the list index
list1[1] = "Harry"
print(list1)

#To delete an element from a list we use the del keyword and the index of the item we wish to delete
del list1[-1]
print(list1)

#We can check if an element is or isn't in a list
print("Christopher" in list1)
print("Christopher" not in list1)

lista = ["Sports", "are", "fun"]
listb = ["Dog", "Turbo dog", "Mega dawg"]
listc = [33, "QAC"]

listlist = [lista, listb, listc, 44, 43.4]

print(listlist[0][1])