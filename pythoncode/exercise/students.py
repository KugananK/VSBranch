class Students:
    def __init__(self, name, age, class_="Student"):
        self.name = name
        self.age = age
        self.class_ = class_
    
    def testscore(self, test1, test2, test3):
        avgscore = (test1 + test2 + test3) / 3
        return format(avgscore, '.2f')

John = Students("John", 22, "22Apr")

print(getattr(John, "name"))
print(getattr(John, "class_"))
print(John.testscore(12,13,15))