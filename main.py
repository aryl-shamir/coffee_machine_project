
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
    }
}


profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO. 2. Check resources sufficient:
def check_resources(ordered_ingredient):
    """ check if there are enough resources to make the selected drink, return
     True if all required ingredients are available in sufficient quantity, False otherwise."""

    for items in ordered_ingredient:
        if ordered_ingredient[items] > resources[items]:
            return False
    return True


def process_coin():
    """Returns the total calculated from coins"""
    print("Please insert coins.")
    total  = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.10
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """ Return True when the payment is accepted, False when the money is insufficient """
    global profit
    if money_received >= drink_cost:
        profit += drink_cost
        remainder = round(money_received - drink_cost, 2)
        print(f"Here is ${remainder} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name , ordered_ingredient):
    """Deduct the required ingredients from the resources."""
    for items in ordered_ingredient:
        resources[items] -= ordered_ingredient[items]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


# TODO. 1. Print the report of all the coffe machine resources.
is_on = True
while is_on:
    Desire = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if Desire == "off":
        print("Turn off the Coffee Machine")
        is_on = False
    elif Desire == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        option = MENU[Desire]
        if check_resources(option["ingredients"]):
            if is_transaction_successful(process_coin(), option['cost']):
                make_coffee(Desire, option["ingredients"])


