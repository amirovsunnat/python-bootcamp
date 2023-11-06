"""
In this project we are going to implement a program to find out whether entered number is prime
"""
import math


# first we will create function for checking
def prime_checker(number):
    if number < 2 or number % 2 == 0:
        return "It's not a prime number."
    for i in range(2, number):
        if number % i == 0:
            return "It's not a prime number."
    return "It's a prime number."


number_ = int(input("Enter number you want to check: "))
print(prime_checker(number=number_))
