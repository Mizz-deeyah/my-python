import random


bids = {}

# STEP 1: Collect bids
bidding = True

while bidding:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid amount: $"))

    bids[name] = bid

    more = input("Are there more bidders? (yes/no): ").lower()
    if more == "no":
       break

# STEP 2: Find winner
highest_bid = 0
winner = ""

for person in bids:
    bid_amount = bids[person]

    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = person

print(f"\nThe winner is {winner} with a bid of {highest_bid}")

# STEP 3: Equipment status
status = input("Enter equipment status: ")

# STEP 4: Store result
equipment = {
    "winner": winner,
    "bid": highest_bid,
    "status": status
}

# STEP 5: Display report
print("\n--- Equipment Report ---")
print(f"Winner: {equipment['winner']}")
print(f"Winning Bid: {equipment['bid']}")
print(f"Status: {equipment['status']}")