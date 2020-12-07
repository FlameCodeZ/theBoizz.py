grade1 = input("Enter your first grade \n")

grade2 = input("Enter your second grade \n")

gradeTot = ((int(grade1) + int(grade2)) / 2)

print(f"Your grade total is {round(gradeTot)}")

if gradeTot >= 85:
    print(":D")
else:
    if gradeTot >= 75:
        print(":)")
    else:
        if gradeTot >= 50:
            print(":/")
        else:
            print(":(")
