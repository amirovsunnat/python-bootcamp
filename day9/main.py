from logo import logo
import os

print(logo)
bidders = {}


def find_winner(bidders_dic):
    max_bidder = 0
    winner = ""
    for bidder in bidders_dic:
        if bidders[bidder] > max_bidder:
            max_bidder = bidders_dic[bidder]
            winner = bidder
    return f"The winner is {winner} ${max_bidder}"


while True:
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))
    bidders[name] = bid
    any_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()
    if any_bidders == "yes":
        os.system('cls')
    else:
        print(find_winner(bidders))
        break

