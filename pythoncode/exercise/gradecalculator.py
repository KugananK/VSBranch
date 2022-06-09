# stuname = input("Enter your name")
# homescore = int(input("Enter homework score"))
# assscore = int(input("Enter assessment score"))
# exscore = int(input("Enter final exam score"))

# def grades(name, hscore, ascore, escore):
# #    #oscore = ((hscore + ascore + exscore) / 175) * 100
#     return f'Student name: {name}, Homework: {(hscore / 25) * 100}% , Assessments: {(ascore / 50) * 100}%, Final exam: {(escore / 100) * 100}%, Overall percentage: {oscore}%'

# print(grades(stuname, homescore, assscore, exscore))

stuname = input("Enter your name")
homescore = float(input("Enter homework score"))
assscore = float(input("Enter assessment score"))
exscore = float(input("Enter final exam score"))
oscore = ((homescore + assscore + exscore) / 175) * 100


def grades(name, oscore):
    return f'Student name: {name}, Overall percentage: {oscore}%'

print(grades(stuname, format(oscore, '.2f')))

#how ryan did it
def grade_calc(homework, assessment, exam):
    mark = (((homework + assessment + exam) / 175) *100)
    return mark

def grade(assessment_mark):
    if assessment_mark > 80:
        return "A"
    elif assessment_mark > 70:
        return "B"
    elif assessment_mark > 60:
        return "C"
    else:
        return "Fail"
    
name = input("Enter your name")
homework1 = int(input("Enter your homework score out of 25: "))
assessment1 = int(input("Enter your assessment score out of 50: "))
exam1 = int(input("Enter your final exam score out of 100: "))

print(f'{name} your final overall percentage is {grade_calc(homework1, assessment1, exam1)} your overall grade is {grade(mark)}')
