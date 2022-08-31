from art import logo
import random

print(logo)

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


