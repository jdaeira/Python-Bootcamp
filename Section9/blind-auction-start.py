import art

from replit import clear
#HINT: You can call clear() to clear the output in the console.
print(art.logo)

bidders = True
bidding_record = {}

while bidders == True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidding_record[name] = bid
    
    choice = input("Are there any other bidders? 'Y' or 'N': ").upper()
    clear()

    if choice == "N":
        max_bid = max(bidding_record.values())
        max_key = max(bidding_record, key=bidding_record.get)
        print(f"The winnder is {max_key} with a bid of ${max_bid}\n")
        bidders = False
       

