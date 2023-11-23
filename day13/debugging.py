############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

"""
on this first problem i never going to be equal to 20. The reason is range goes until end not including the endpoint.
"""

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

from random import randint

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 5)  # should 5 not 6.
print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

year = int(input("What's your year of birth?"))
if 1980 < year < 1994:  # in here if year is less than 1980 it is not going to print anything
    print("You are a millenial.")
elif year < 1980:  # add this condition to handle any number inputs
    print("You are oldenial")
elif year > 1994:
    print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

age = int(input("How old are you?"))  # convert to integer
if age > 18:
    print("You can drive at age {age}.")  # indent

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# remove to defined variables with the same names
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))  # remove second = sign it is checking for
# equality not assigning value
total_words = pages * word_per_page
print(total_words)


# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])


def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)  # it is only adding last item on the a_list because it is not inside of loop
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
