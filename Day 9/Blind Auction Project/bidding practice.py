bids ={}

import art
print(art.logo)

while True:
    name = input("Enter your name: ")
    bid =int(input("your bid: $ "))
    bids[name]=bid


    more_bidders =input("are there  any more bidders? (yes or 'no'): ")
    if more_bidders== "no":
        break
highest_bid = 0
winner = ""
for person in bids:
            if bids[person] > highest_bid:
                highest_bid = bids[person]
                winner = person
            print(f"winner is {winner}, with a bid of {highest_bid}")
