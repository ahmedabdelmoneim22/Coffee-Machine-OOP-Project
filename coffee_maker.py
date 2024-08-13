#>>class CoffeeMaker That Make Coffee.
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        #>>Initialize coffee Machine ingredients resources.
        self.resources = {
            "water": 600,
            "milk": 400,
            "coffee": 200,
        }
    #>>Make Class function report To Print All Ingredients resources.
    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
    #>>Chicking if resource sufficient to Make Coffee Drink.
    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make
    #>>Class function make_coffee and[ resources - item ingredients ].
    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
#>>By Ahmed-AbdelMoneim.
