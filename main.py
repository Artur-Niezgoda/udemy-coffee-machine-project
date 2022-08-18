def print_report(profit):
    """Print contents of resources and amount of money in the machine.

    Args:
        profit (float): the profit of the machine
    """
    for key, value in resources.items():
            print(f"{key.capitalize()}: {value}")
    print(f"Profit: ${profit}")



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
    
                
            