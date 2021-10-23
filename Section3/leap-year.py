year = int(input("Please enter a year: "))

if year % 4 == 0 and year % 400 == 0:
    print("This ia a leap year!")
elif year % 4 == 0 and year % 100 != 0:
    print("This is a leap year!")
elif year % 100 == 0 and year % 400 == 0:
    print("This is a leap year!")
else:
    print("That is not a leap year!")