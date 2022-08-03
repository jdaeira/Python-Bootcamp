print("Welcome to the Roller Coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the Roller Coaster!")
    age = int(input("What is your age? "))
    if age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
    elif age > 18 :
        bill = 12
        print("Adult tickets are $12")
    elif age >= 12 and age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 5
        print("Child tickets are $5")

    wants_photo = input("Do you want a photo? Y or N. ")
    if wants_photo.upper() == "Y":
        bill += 3
    
    print(f"Your final bill is ${bill}")
            
else:
    print("Sorry, but you are too short to ride the Roller Coaster.")