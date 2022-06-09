mark = float(input("Your exam mark?"))

if mark >= 65:
    if mark >= 85:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")