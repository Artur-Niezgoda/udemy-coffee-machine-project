from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


cafe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True


while is_on:
    drink = None
    while drink == None:
        print(f"What would you like to drink? Here are the options: {menu.get_items()}\n")
        drink = input()
        if drink == "report":
            cafe_maker.report()
            money_machine.report()
        elif drink == "off":
            is_on = False
        drink = (menu.find_drink(drink))
    if cafe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            cafe_maker.make_coffee(drink)
        