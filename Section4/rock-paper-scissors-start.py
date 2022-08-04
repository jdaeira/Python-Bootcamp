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

#Write your code below this line 
images = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if user > len(images) - 1 or user < 0:
    print("That's an invalid entry. You Lose!")
    exit()

print(images[user])

computer = random.randint(0, 2)

print("Computer chose:")

print(images[computer])

if user == computer:
    print("It's a Draw!")
elif (user == 0 and computer == 2) or (user == 2 and computer == 1) or (user == 1 and computer == 0):
    print("You Win!")
else:
    print("You Lose!")

