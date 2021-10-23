
print("Welcome to the Roller Coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the Roller Coaster!")
    age = int(input("What is your age? "))
    if age > 18:
        print("You need to pay $12")
    elif age >= 12 and age <= 18:
        print("You need to pay $7")
    else:
        print("You need to pay $5")
else:
    print("Sorry, but you are too short to ride the Roller Coaster.")