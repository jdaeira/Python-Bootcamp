from art import logo, vs
from game_data import data
import random

numberA = random.randint(0, len(data) - 1)
numberB = random.randint(0, len(data) - 1)
print(numberA)
print(numberB)

while numberB == numberA:
    numberB = random.randint(0, len(data) - 1)

print(numberA)
print(numberB)

print(data[numberA]["follower_count"])
print(data[numberB]["follower_count"])
print(len(data))

print(logo)

print(f"Compare A: {data[numberA]['name']}, a {data[numberA]['description']}, from {data[numberA]['country']}")

print(vs)

print(f"Compare B: {data[numberB]['name']}, a {data[numberB]['description']}, from {data[numberB]['country']}")

more = input("Who has more followers? Type 'A' or 'B': ").upper()
print(more)