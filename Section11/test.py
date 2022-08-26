cards = [11, 11]

count = 0
for i in cards:
    if 11 in cards:
        cards[count] = 1
        count += 1
        exit()

print(cards)
