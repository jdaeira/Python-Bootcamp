cards = [11, 11, 11, 9]

for i in range(len(cards)):
    if cards[i] == 11 and sum(cards) > 21:
        cards[i] = 1
    

print(cards)
