import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

## Create a list of the ascii images
images = [rock, paper, scissors]

## Gets the input from the user
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

## Checks to see if the inputed value is valid or now
if user > len(images) - 1 or user < 0:
    print("That's an invalid entry. You Lose!")
    exit()
## Print the image the user chose
print(images[user])

## Computer chooses a random number
computer = random.randint(0, 2)

print("Computer chose:")

## Print the image the computer chose
print(images[computer])

## Checks to see who won the Game
if user == computer:
    print("It's a Draw!")
elif (user == 0 and computer == 2) or (user == 2 and computer == 1) or (user == 1 and computer == 0):
    print("You Win!")
else:
    print("You Lose!")

