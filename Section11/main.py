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
user_score = 0
dealer_score = 0
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

def play_game():
    global user_score
    global dealer_score

    user_score = get_score(user_cards)
    dealer_score = get_score(dealer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {dealer_cards[0]}")

    if dealer_score == 21 and user_score == 21:
        print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
        print("Push! No One Wins")
        exit()
    elif dealer_score == 21 and user_score != 21:
        print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
        print("Dealer Wins!")
        exit()

    deal_cards = True
    while deal_cards == True:
        more_cards = input("Would you like another card? Type 'y' or 'n': ").lower()

        if more_cards == "y":
            get_cards("user", 1)
            user_score = get_score(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(dealer_cards[0])
        else:
            deal_cards = False
            
    print(f"Your final hand: {user_cards}, final score: {user_score}")

    while dealer_score < 17:
        get_cards("dealer", 1)
        dealer_score = get_score(dealer_cards)

    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")

    test_function()

def test_function():
    dealer_score = 25
    user_score = 23
    print(dealer_score)
    print(user_score)


print(logo)
play = True
while play == True:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    
    user_cards = []
    dealer_cards = []

    if choice == "y":
       get_cards("user", 2)
       get_cards("dealer", 2)
       play_game()
    else:
       play = False