books = {"Rowling" : ["Harry Potter1", "Harry Potter3", "Harry Potter2"], "Tolkien" : ["Hobbit", "Lord of the Rings"],  "Roald Dahl" : ["Chocolate Factory","Giant Peach"]}
name = input("Enter an author name")

books[name].sort()
# output = ", ".join(books[name])
# print(output)
print(", ".join(books[name]))

# my_dict = {"a": 3, "b": 9, "c": 16}
#     if value == 9:
#         print(key)
# Not sure what this is but he showed it