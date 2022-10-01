from art import logo, vs
from game_data import data
import random

numberA = random.randint(0, len(data) - 1)

score = 0
win = True

while win == True:

    numberB = random.randint(0, len(data) - 1)
    while numberB == numberA:
        numberB = random.randint(0, len(data) - 1)

    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")

    print(f"Compare A: {data[numberA]['name']}, a {data[numberA]['description']}, from {data[numberA]['country']}")

    print(vs)

    print(f"Compare B: {data[numberB]['name']}, a {data[numberB]['description']}, from {data[numberB]['country']}")

    more = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    if more == "A":
        if data[numberA]["follower_count"] > data[numberB]["follower_count"]:
            score += 1
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            win = False
    elif more == "B":
        if data[numberB]["follower_count"] > data[numberA]["follower_count"]:
            score += 1
            numberA = numberB
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            win = False

print()
