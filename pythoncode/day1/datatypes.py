name = "Ryan, Paul, Wright"

# str.lower() converts string to lowercase
print(name.lower())
# str.upper() converts string to uppercase
print(name.upper())
#str.replace replaces old substring with new
print(name.replace("Paul", "Dragon"))
#str.split returns a list of words in the string, we can specify the seperator inside the parenthesis
print(name.split(" , "))
#str.join concatenate an iterable or collection of strings
print(" space ".join(["Ryan", "Paul", "Wright"]))
#str.count() returns number of non overlapping occurances of substring in string
print(name.count("a"))
#str.isdigit() returns true if string contains digit, false otherwise
str1 = "cat" # false
str2 = "123" # true
str3 = "12.34" # false
print(str1.isdigit())
print(str2.isdigit())
print(str3.isdigit())

# Concatination combining strings togeter
print("cat" + "dog") # Returns catdog
print("cat" , "dog") # Returns cat dog

school = "High"
age = 600
maths = True
testscore = 66.9

print("My name is", name, "My age is", age, "Maths :", maths, "My test score is", testscore)
# f strings allow us to combine multiple datatypes in a string as well as perform calculations within curly brackets
print(f'My name is {name}, My age is {age - 569}, MAths : {maths}, My test score is {testscore}')

print("Hello my name is \"Ryan\"")
#prints Hello my name is "Ryan", the backslash is a wildcard charecter
print("my name is \\Ryan\\")
#prints my name is \Ryan\
print("Hello \nMy name is Ryan")
#prints Hello
#Myname is Ryan
#\n is new line
print("Hello \tMy name is Ryan")
#prints Hello    My name is Ryan
#\t is indent or tab