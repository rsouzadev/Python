while True:
    year = int(input("Please inform the year:"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Leap!")
    else:
        print("Not Leap!")
    option = str(input("Would you like to continue?[Y/N]")).strip().upper()
    if option in "Yy":
        print("OK Let's go!")
    else:
        break
