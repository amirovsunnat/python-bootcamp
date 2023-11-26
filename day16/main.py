from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# create objects from classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while True:
    # get all the coffee names
    drinks = menu.get_items()
    user_choice = input(f"What would like to order ({drinks}): ").strip().lower()
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        break
    # checks if user choice is in coffee names
    elif user_choice in drinks:
        coffee = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)
    # if user choice is not valid then we show this message
    else:
        print("Please enter valid coffee name")
