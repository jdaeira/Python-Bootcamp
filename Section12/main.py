from art import logo
import random

print(logo)

#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

#Welcome to the Number Guessing Game!
# I'm thinking of a number between 1 and 100.
# Choose a difficulty. Type 'easy' or 'hard':
# You have 5 attempts remaining to guess the number.
# Make a guess:
# Too HIGH
# Guess again
# You have 4 attempts remaining to guess the number

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 101)
print(f"Pssst, the correct answer is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

attempts = 0
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

winner = False
while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
    if guess == number:
        print("You Guessed the correct number!")
        attempts = 0
        winner = True
    elif guess > number:
        print("Too High.")
        attempts -= 1
        if attempts > 0:
            print("Guess Again.")
    elif guess < number:
        print("Too Low.")
        attempts -= 1
        if attempts > 0:
            print("Guess Again.")

if winner == False:
   print("You've run out of guesses, you lose.")        


