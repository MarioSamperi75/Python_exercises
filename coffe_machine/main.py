from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


is_on = True
while is_on:
    choice = input(" What would you like? (espresso/latte/cappuccino): ")
    if choice.lower() == "off":
        is_on = False
    elif choice.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(menu_item):
            money_machine.make_payment(menu_item.cost)
            coffee_maker.make_coffee(menu_item)

