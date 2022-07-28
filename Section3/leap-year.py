year = int(input("Please enter a year: "))

if year % 4 == 0 and year % 400 == 0:
    print("This ia a leap year!")
elif year % 4 == 0 and year % 100 != 0:
    print("This is a leap year!")
elif year % 100 == 0 and year % 400 == 0:
    print("This is a leap year!")
else:
    print("That is not a leap year!")

   
year1 = int(input("Please enter a year to check: "))

if year1 % 4 == 0:
    if year1 % 100 == 0:
        if year1 % 400 == 0:
            print("Leap Year!")
        else:
            print("Not Leap Year!")
    else:
        print("Leap Year!")
else:
    print("Not Leap Year!")