import os
from art import logo, vs
from game_data import data
from random import choice


def format_info(account):
    """Takes instagram account and returns formatted way."""
    if account['description'][0] in ['a', 'e', 'i', 'o', 'u']:
        article = 'an'
    else:
        article = 'a'
    return f"{account['name']}, {article} {account['description']}, from {account['country']}"


def compare_accounts(user_guess, account1_followers, account2_followers):
    """Takes user guess and numbers of follower counts of both accounts. Compare them, and returns true or false."""
    if account1_followers > account2_followers:
        # returns true if user guessed a, otherwise false
        return user_guess == "a"
    else:
        # returns true if user guessed b, otherwise false
        return user_guess == "b"


account_b = choice(data)
user_score = 0
print(logo)

while True:
    account_a = account_b

    while account_a == account_b:
        account_b = choice(data)

    print(f"Compare A: {format_info(account_a)}")
    print(vs)
    print(f"Against B: {format_info(account_b)}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
    does_user_right = compare_accounts(user_guess=guess, account1_followers=account_a['follower_count'], account2_followers=account_b['follower_count'])
    os.system("cls")
    print(logo)
    if does_user_right:
        user_score += 1
        print(f"You are right! Youre current score: {user_score}")
    else:
        print(f"You guess is wrong. Your final score: {user_score}")
        break
    

