MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def is_resource_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
while True:
    choice = input("what would you like? (espresso/latte/cappuccino):\n").lower()

    if choice == "off":
        break

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")

    elif choice in MENU:
        drink = MENU[choice]

        if is_resource_sufficient(drink["ingredients"]):

            payment = process_coins()

            if payment >= drink["cost"]:
                change = round(payment - drink["cost"], 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice}. Enjoy!")

                resources["money"] += drink["cost"]

                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]

            else:
                print("Sorry that's not enough money. Money refunded.")