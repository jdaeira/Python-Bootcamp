import random
from webbrowser import get
from art import logo
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Initialize Global Variables
user_cards = []
dealer_cards = []
user_score = 0
dealer_score = 0

#This Function deals the cards for the player and computer
def get_cards(player_type, num_cards):
    if player_type == "user":
        for _ in range(num_cards):
            card = random.randint(0, 12)
            user_cards.append(cards[card])
    else:
        for _ in range(num_cards):
            card = random.randint(0, 12)
            dealer_cards.append(cards[card])

#This Function checks is there are Aces in the deck and deals with them
def check_aces(player_type):
    if player_type == "user":
        for i in range(len(user_cards)):
            if user_cards[i] == 11 and sum(user_cards) > 21:
               user_cards[i] = 1
                
    else:
        for i in range(len(dealer_cards)):
            if dealer_cards[i] == 11 and sum(dealer_cards) > 21:
               dealer_cards[i] = 1
                
#This function get the score for the player or computer
def get_score(player_list):
    score = sum(player_list)
    return score

#This Function checks if there is a winner for the first part of them game
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
    elif dealer_score == 21 and user_score != 21:
        print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
        print("Dealer Wins!")
    elif user_score == 21 and dealer_score != 21:
        print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
        print("You Win!")
    else:
        deal_cards()

#This Function deals more cards if no one wins in the initial deal of cards
def deal_cards():
    global user_score
    global dealer_score

    deal_cards = True
    while deal_cards == True:
        more_cards = input("Would you like another card? Type 'y' or 'n': ").lower()

        if more_cards == "y":
            get_cards("user", 1)
            check_aces("user")
            user_score = get_score(user_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(dealer_cards[0])
        else:
            deal_cards = False
            
    print(f"Your final hand: {user_cards}, final score: {user_score}")

    while dealer_score < 17:
        get_cards("dealer", 1)
        check_aces("dealer")
        dealer_score = get_score(dealer_cards)

    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")

    check_winner()

#This Function checks if there is a winner
def check_winner():
    global user_score
    global dealer_score

    if user_score > dealer_score and user_score < 22:
        print("You Win!")
    elif dealer_score > user_score and dealer_score < 22:
        print("Dealer Wins!")
    elif user_score < 22 and dealer_score > 21:
        print("You Win!") 
    elif dealer_score < 22 and user_score > 21:
        print("Dealer Wins!")
    elif dealer_score == user_score and user_score < 22 and dealer_score < 22:
        print("Push!")
    elif dealer_score > 21 and user_score > 21:
        print("Both Busted! Nobody Wins")

#Start of the game
print(logo)
play = True
while play == True:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    
    user_cards = []
    dealer_cards = []

    if choice == "y":
       get_cards("user", 2)
       check_aces("user")
       get_cards("dealer", 2)
       check_aces("dealer")
       play_game()
    else:
       print("Good Bye! Thank You for Playing!")
       play = False