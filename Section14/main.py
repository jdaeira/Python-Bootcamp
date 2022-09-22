from art import logo, vs
from game_data import data
import random

numberA = random.randint(1, len(data) + 1)

print(data[numberA]["follower_count"])
print(len(data))

print(logo)

print(f"Compare A: {data[numberA]['name']}, a {data[numberA]['description']}, from {data[numberA]['country']}")

