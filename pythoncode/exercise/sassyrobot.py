name = input("Your name....")
named = input("Stop mumbling and say it again")
age = int(input("enter age as integer"))
testscore1 = input("enter first test result as float")
testscore2 = input("enter second test result as float")

float_number = float(testscore1)
float_number2 = float(testscore2)

if float(testscore1) > 6:
    passed = True
else:
    passed = False
    print("You failed a test smh")

if float(testscore2) > 6:
    passed2 = True
else:
    passed2 = False
    print("You failed a test smh")


print(f'Hello {named}, I know you are not {age + 1} yet but you need to speak up')
print("Statement: ", testscore1, "Passed?", passed)
print("Statement: ", testscore2, "passed?", passed2)