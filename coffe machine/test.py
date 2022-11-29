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

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_sufficient(drinks):
    for i in drinks:
        if drinks[i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


def process_coin():
    print("Please insert coins.")
    total = float(input("how many Quarters?: ")) * 0.25
    total += float(input("how many Dimes?: ")) * 0.10
    total += float(input("how many Nickels?: ")) * 0.05
    total += float(input("how many Pennies?: ")) * 0.01
    return total


def check_transaction(payment, cost):
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffe(drink_name, drinks):
    for i in drinks:
        resources[i] -= drinks[i]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


on = True
while on:
    drinks_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if drinks_choice == "off":
        on = False
    elif drinks_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drinks = MENU[drinks_choice]
        if resources_sufficient(drinks["ingredients"]):
            payment = process_coin()
            if check_transaction(payment, drinks['cost']):
                make_coffe(drinks_choice, drinks["ingredients"])


