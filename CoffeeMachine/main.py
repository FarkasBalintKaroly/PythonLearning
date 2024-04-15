MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    "latte-macchiato": {
        "ingredients": {
            "water": 0,
            "milk": 150,
            "coffee": 100,
        },
        "cost": 0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1. Print report of all coffee machine resources.
def report(profit):
    """Prints a report about resources."""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {profit}")


# TODO: 2. Check resources are sufficient.
def enough_resources(coffee_type):
    """Check if there is enough resources."""
    ingredients_list = MENU[coffee_type]["ingredients"]
    for ingredients in ingredients_list:
        if ingredients_list[ingredients] > resources[ingredients]:
            print(f"There is not enough {ingredients}!")
            return False
    return True


# TODO: 3. Process coins.
def processing_coins(quarters, dimes, nickles, pennies):
    """Summarizes all the coins dropped in."""
    sum_money = 0
    sum_money += quarters * 0.25
    sum_money += dimes * 0.1
    sum_money += nickles * 0.05
    sum_money += pennies * 0.01
    return sum_money


# TODO: 4. Check transaction successful.
def transaction_successful(user_choice):
    """Check if the transaction was successful."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    inserted_coins = processing_coins(quarters, dimes, nickles, pennies)
    coffee_price = MENU[user_choice]["cost"]
    if inserted_coins >= coffee_price:
        if inserted_coins > coffee_price:
            refund = inserted_coins - coffee_price
            formated_refund = "{:.2f}".format(refund)
            print(f"Here is ${formated_refund} dollars in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def deducing_ingredients(coffee_type):
    """Deducing resources."""
    ingredients_list = MENU[coffee_type]["ingredients"]
    for ingredients in ingredients_list:
        resources[ingredients] -= ingredients_list[ingredients]
    print(f"Here is your {coffee_type}! Enjoy!")


def coffee_machine():
    should_continue = True
    profit = 0.00

    while should_continue:
        user_choice = input("What would you like? (espresso/latte/cappuccino/latte-macchiato): ").lower()
        if user_choice == "report":
            report(profit)
        elif user_choice == "off":
            print("Coffee machine is turning off...")
            should_continue = False
            return
        elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino" or user_choice == "latte-macchiato":
            if enough_resources(user_choice):
                if transaction_successful(user_choice=user_choice):
                    coffee_price = MENU[user_choice]["cost"]
                    profit += coffee_price
                    deducing_ingredients(coffee_type=user_choice)
            else:
                return


coffee_machine()
