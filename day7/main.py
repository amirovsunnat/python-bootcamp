import random
from stages import stages, logo
from hangman_words import word_list

# creating variables for lives, random word, and list of letter
lives = 6
random_word = random.choice(word_list)
list_of_letters = []
print(random_word)

# adding _ for list of letters as much as length of the random word
for i in range(len(random_word)):
    list_of_letters.append("_")

# printing logo
print(logo)

# taking user input and checking if user can guess correctly the random word
while True:
    user_guess = input("Guess a letter: ").lower()
    # if user guessed the same letter we are telling it
    if user_guess in list_of_letters:
        print(f"You've already guessed {user_guess}")
    # looping through word and checking if user guess matches
    for i in range(len(random_word)):
        if user_guess == random_word[i]:
            list_of_letters[i] = user_guess
    # if not we are omitting one life
    if user_guess not in random_word:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life.")
        print(stages[lives])
        lives -= 1
    if lives < 0:
        print("You lose")
        break
    # in every iteration we are showing list of letters
    print(list_of_letters)

    # check if the user guessed all the letters correctly
    if "_" not in list_of_letters:
        break

# finally checking if random word matches or not
if "".join(list_of_letters) == random_word:
    print("You win!")

