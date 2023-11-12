import os
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []


def game():
    while True:
        want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower()
        if want_to_play == "y":
            user_cards.append(random.choice(cards))
            user_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")
            want_to_get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if want_to_get_another_card == "y":
                user_cards.append(random.choice(cards))
                print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
                print(f"Computer's first card: {computer_cards[0]}")
            print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            if 21 >= sum(user_cards) > sum(computer_cards):
                print("You win")
            else:
                print("You went over. You lose 😤")
                user_cards.clear()
                computer_cards.clear()
                os.system("cls")
        else:
            break


game()
