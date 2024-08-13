print("Coffee-Machine-OOP-Project")
from menu import Menu, MenuItem #Import Class Menu and MenuItem From menu File.
from coffee_maker import CoffeeMaker #Import Class CoffeeMaker From coffee_maker File.
from money_machine import MoneyMachine #Import Class MoneyMachine From money_machine File.
money_machine = MoneyMachine()#>>Create Instance from class MoneyMachine().
coffee_maker = CoffeeMaker()#>>Create Instance from class CoffeeMaker().
menu = Menu()#>>Create Instance from class Menu().
#>>Infinite-Loop-break-IF-User-Input-off.
while True:
    print(menu.menu[0].name,"price is",menu.menu[0].cost,"$")
    print(menu.menu[1].name, "price is", menu.menu[1].cost,"$")
    print(menu.menu[2].name, "price is", menu.menu[2].cost,"$")
    #>>Ask User Input Coffee Type ?
    input_user=input(f"What would you like? ({menu.get_items()}): ").lower()
    #>>report Get coffee-Machine ingredients&Money details.
    if input_user=="report":
        coffee_maker.report()
        money_machine.report()
    #>>If User Input off Stop The-coffee-Machine.
    elif input_user=="off":
        break
    else:
        #>>Chicking that Item in coffee-Machine Drinks.
        m = menu.find_drink(input_user)
        #>>Initialize The Input Drink Items.
        menu_item = MenuItem(name=m.name,
                             water=m.ingredients["water"],
                             milk=m.ingredients["milk"],
                             coffee=m.ingredients["coffee"],
                             cost=m.cost)
        #>>Chick if menu_item is sufficient To Make Drink.
        if coffee_maker.is_resource_sufficient(menu_item):
            #>>Chick if user Have Enough Money To Get Drink.
            #>>money_machine.make_payment(cost=menu_item.cost)
            #>>If User Have Enough Money Get The Drink.
            if money_machine.make_payment(cost=menu_item.cost):
                coffee_maker.make_coffee(menu_item)
#>>By Ahmed-AbdelMoneim.

