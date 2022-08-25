while True:
    year = int(input("Please inform the year:"))
    if year % 4 == 0:
        print("Leap!")
    elif year % 100 == 0:
        print("Leap!")
    elif year % 100 != 0:
        print("Not Leap!")
    elif year % 4 == 0:
        print("Leap!")
    else:
        print("Not Leap!")
    option = str(input("Do you want to continue[Y/N]?")).strip().upper()
    if option in "Yy":
        print("Ok! Let's go!")
    else:
        break
