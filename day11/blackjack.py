import os
import random
from logo import logo


def deck_card():
    """Returns a random card from cards."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Takes a list of cards, calculate them, and returns sum"""
    # if cards sum is 21 and length is 2 we are returning 0
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # if 11 inside cards and sum is over than 21 we are replacing 11 with 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_score(score_user, score_comp):
    """Compares user and computer score and returns message regarding result"""
    if score_comp > 21 and score_user > 21:
        return "No one win."
    if score_user == score_comp:
        return "Draw 🙃"
    elif score_user == 0:
        return "Win with a Blackjack 😎"
    elif score_comp == 0:
        return "Lose, opponent has Blackjack 😱"
    elif score_user > 21:
        return "You went over. You lose 😭"
    elif score_comp > 21:
        return "Opponent went over. You win 😁"
    elif score_user > score_comp:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_blackjack():
    """Blackjack play function"""
    print(logo)
    user_cards = []
    computer_cards = []

    # we are adding random cards to our user and computer cards
    for _ in range(2):
        user_cards.append(deck_card())
        computer_cards.append(deck_card())

    game_is_over = False
    while not game_is_over:
        # calculating user and computers cards
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # check either of them have blackjack or user cards are more than 21
        if user_score == 0 or user_score > 21 or computer_score == 0:
            game_is_over = True
        else:
            want_to_deck = input("Type 'y' to get another card, type 'n' to pass: ")
            if want_to_deck == "y":
                user_cards.append(deck_card())
            else:
                game_is_over = True

    # add cards until computer cards less than 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deck_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))


# while user want to play the game will go on
while True:
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_to_play == "y":
        # if you want to play we clear the console
        os.system("cls")
        play_blackjack()
    else:
        break



