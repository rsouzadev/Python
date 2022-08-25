while True:
    year = int(input("Please inform the year:"))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap Year!")
            else:
                print("Not Leap!")
        else:
            print("Leap!")
    else:
        print("Not Leap!")
    option = str(input("Do u wanna continue pal?[Y/N]")).strip().upper()
    if option in "Yy":
        print("Alright my nigga!")
    else:
        break
