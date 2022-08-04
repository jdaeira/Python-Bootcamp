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

#Write your code below this line 👇
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if user == 0:
    print(rock)
elif user == 1:
    print(paper)
else:
    print(scissors)

computer = random.randint(0, 2)

print("Computer chose:")

if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

if user == 0 and computer == 0:
    print("It's a Draw!")
elif user == 1 and computer == 1:
    print("It's a Draw!")
elif user == 2 and computer == 2:
    print("It's a Draw!")


if (user == 0 and computer == 2) or (user == 2 and computer == 1) or (user == 1 and computer == 0):
    print("You Win!")
elif (computer == 0 and user == 2) or (computer == 2 and user == 1) or (computer == 1 and user == 0):
    print("You Lose!")