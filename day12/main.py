import random
import logo


def choose_level():
    """User chooses a level, and based on that it returns attempts."""
    lives = 0
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
    if level == "easy":
        lives = 10
    elif level == "hard":
        lives = 5
    else:
        print("Please choose valid level.")
    return lives


attempts = choose_level()


def number_guess():
    """User guess number until number has been correctly or no attempts left"""
    print(logo.logo)
    print("Welcome to the number guessing game.")
    print("I'm thinking a number between 1 to 100.")
    global attempts
    random_number = random.randint(1, 100)
    while True:
        attempts -= 1
        user_guess = int(input("Make a guess: "))
        if random_number == user_guess:
            print(f"You win. The answer was {random_number}")
            break
        elif random_number > user_guess:
            print("Too low")
            print("Guess again")
        elif random_number < user_guess:
            print("Too high")
            print("Guess again")
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            break
        else:
            print(f"You have {attempts} remaining to guess the number")


number_guess()
