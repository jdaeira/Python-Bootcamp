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
dealer_cards = []
def get_cards(player_type, num_cards):
    if player_type == "user":
        for _ in range(num_cards):
            card = random.randint(0, 12)
            user_cards.append(cards[card])
    else:
        for _ in range(num_cards):
            card = random.randint(0, 12)
            dealer_cards.append(cards[card])

def get_score(player_list):
    score = sum(player_list)
    return score




print(logo)
play = True
while play == True:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    
    user_cards = []
    dealer_cards = []

    if choice == "y":
        get_cards("user", 2)
        get_cards("dealer", 2)
        print(user_cards)
        print(dealer_cards)
        print(dealer_cards[0])
        print(get_score(user_cards))
        print(get_score(dealer_cards))
    else:
        play = False