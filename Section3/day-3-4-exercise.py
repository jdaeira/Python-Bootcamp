print("Welcome to the Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

total = 0

if size.upper() == "S":
    total += 15
elif size.upper() == "M":
    total += 20
else:
    total += 25

if add_pepperoni.upper() == "Y":
    if size.upper() == "S":
        total += 2
    else:
        total += 3

if extra_cheese.upper() == "Y":
    total += 1

print(f"Your final bill is: ${total}")