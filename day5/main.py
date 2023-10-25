"""
Password generator
"""

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n>>> "))
nr_symbols = int(input(f"How many symbols would you like?\n>>> "))
nr_numbers = int(input(f"How many numbers would you like?\n>>> "))
password_string = ""


def generate_random_elements(number_of_elements, list_of_elements):
    elements_generated = []
    for _ in range(number_of_elements):
        elements_generated.append(random.choice(list_of_elements))
    return elements_generated


password = (generate_random_elements(nr_letters, letters) + generate_random_elements(nr_symbols, symbols) +
            generate_random_elements(nr_numbers, numbers))


random.shuffle(password)
for i in password:
    password_string += i
print(password_string)
