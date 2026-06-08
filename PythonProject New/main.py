from menu import MENU, MenuItem
from cofee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine= MoneyMachine()
cofee_maker = CoffeeMaker()


while is_on:
    options = menu.get_items()
    choice = input("what would you like? ({options}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        cofee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if cofee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            cofee_maker.make_cofee(drink)
            
