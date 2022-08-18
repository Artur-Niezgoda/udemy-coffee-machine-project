def print_report(profit):
    """Print contents of resources and amount of money in the machine.

    Args:
        profit (float): the profit of the machine
    """
    for key, value in resources.items():
            print(f"{key.capitalize()}: {value}")
    print(f"Profit: ${profit}")


def check_resources(resources, ingredients):
    """Check if there is sufficient amount of resources to prepare the order.
    If not, print the list of insufficient ingredients

    Args:
        resources (dict): dictionary of resources available in the coffee machine
        ingredients (dict): dictionary of ingredients required to preapre the order

    Returns:
        boolean: returns True if there is enough resources to prepare the order, False otherwise
    """
    is_enough = True
    for key, val in ingredients.items():
        if resources[key] < val:
            print(f"Sorry there is not enough {key}.")
            is_enough = False
    return is_enough


def get_money():
    """Take the amount of coins and calculate total credit.

    Returns:
        float: the total credit calculated based of number of coins inserted to the machine
    """
    print("Please enter coins.")
    total = 0
    for item, value in coins.items():
        total += value*int(input(f"Number of {item}: "))
    return total


def update_resources(resources, ingridients):
    for key, val in ingridients.items():
        resources[key] -= val
    return resources


def make_coffee():
    """Update resources of the coffee machine and print the change if any.
    """
    amount -= MENU[users_choice]["cost"]
    profit += MENU[users_choice]["cost"]
    resources = update_resources(resources, MENU[users_choice]["ingredients"])
    print(f"Here is your {users_choice}. Enjoy!")
    if amount > 0:
        print(f"Here is ${amount:.2f} dollars in change.")


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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickels": 0.05,
    "pennies": 0.01
}

is_on = True
profit = 0

while is_on:
    users_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if users_choice == "off":
        is_on = False

    if users_choice == "report":
        print_report(profit)
    else:
        if check_resources(resources, MENU[users_choice]["ingredients"]):
            amount = get_money()
            if amount<MENU[users_choice]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
                amount = 0
            else:
                make_coffee(users_choice)
                
            