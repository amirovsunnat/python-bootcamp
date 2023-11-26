from data import MENU, resources

money = 0


def calculate_coins():
    """Calculate total inserted coins, and returns as a total money."""
    print("Please insert coins.")
    quarters = int(input("how many quarters want to insert?: "))
    dimes = int(input("how many dimes want to insert?: "))
    nickles = int(input("how many nickles want to insert?: "))
    pennies = int(input("how many pennies want to insert?: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


def is_payment_successful(total_money_received, coffee_cost):
    """Takes total money received from user and coffee cost, return true if transaction was successful,
    otherwise False."""
    global money
    if total_money_received >= coffee_cost:
        change = round(total_money_received - coffee_cost, 2)
        print(f"Here is ${change} in change")
        money = money + coffee_cost
        return True
    else:
        print("Sorry, that is not enough money. Payment is refunded.")
        return False


def is_resources_enough(coffee_ingredients):
    """Takes resources, and returns true if enough otherwise false and tells which resource is not enough."""
    for ingredient in coffee_ingredients:
        if coffee_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is no enough {ingredient}.")
            return False
    return True


def report(source):
    """Takes source and returns information about source."""
    print(f"Water: {source['water']}ml,\n"
          f"Milk: {source['milk']}ml,\n"
          f"Coffee: {source['coffee']}g,\n"
          f"Money: ${money}")


def make_coffee():
    """Takes user input and makes coffee if resources are enough."""
    while True:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        if user_choice == "report":
            report(source=resources)
        elif user_choice == "off":
            break
        else:
            coffee_type = MENU[user_choice]
            if is_resources_enough(coffee_ingredients=coffee_type['ingredients']):
                payment = calculate_coins()
                if is_payment_successful(total_money_received=payment, coffee_cost=coffee_type['cost']):
                    # if payment is successful we deduct coffee ingredients from resources
                    for ingredient in resources:
                        resources[ingredient] -= coffee_type['ingredients'][ingredient]
                    print(f"Here is your {user_choice} ☕. Enjoy it 😊.")


make_coffee()
