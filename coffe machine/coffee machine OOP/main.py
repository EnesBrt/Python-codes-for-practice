from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Menu = Menu()
CoffeeMaker = CoffeeMaker()
MoneyMachine = MoneyMachine()

on = True
while on:
    options = Menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        on = False
    elif choice == "report":
        CoffeeMaker.report()
        MoneyMachine.report()
    else:
        drink = Menu.find_drink(choice)
        if CoffeeMaker.is_resource_sufficient(drink) and MoneyMachine.make_payment(drink.cost):
            CoffeeMaker.make_coffee(drink)



