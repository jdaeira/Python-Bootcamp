import random
from webbrowser import get
from art import logo
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

user_cards = []
def get_cards():
    for num in range(2):
        card = random.randint(0, 12)
        user_cards.append(cards[card])



print(logo)

play = True

while play == True:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    get_cards()
    print(user_cards)