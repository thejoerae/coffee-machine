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

# money variable to globally keep track of the till
money = 0

# Define coins with constants
PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25

# create variable to turn the coffee machine off and exit the program
coffee_machine_on = True


# create function for change. input pennies, nickels, dimes, quarters, and price of the drink. return change
# or -1 for a failed transaction


def change(pennies, nickels, dimes, quarters, price):
    transaction = (pennies * PENNY) + (nickels * NICKEL) + (dimes * DIME) + (quarters * QUARTER)
    if transaction >= price:
        change_back = transaction - price
        return change_back
    else:
        return -1


# Print a report of all the coffee machine resources


def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


# Check resources against coffee selected


def check_resources(coffee_selected):
    have_enough_stuff = True
    item = MENU[f"{coffee_selected}"]["ingredients"]

    if item["water"] >= resources["water"]:
        print("Sorry there is not enough water.")
        have_enough_stuff = False
    if item["coffee"] >= resources["coffee"]:
        print("Sorry there is not enough coffee.")
        have_enough_stuff = False
    if item.get("milk") is not None:
        if item["milk"] >= resources["milk"]:
            print("Sorry there is not enough milk.")
            have_enough_stuff = False

    if have_enough_stuff:
        return True
    else:
        return False


def deduct_resources(coffee_selected):
    item = MENU[f"{coffee_selected}"]["ingredients"]
    resources["water"] -= item["water"]
    resources["coffee"] -= item["coffee"]
    if item.get("milk") is not None:
        resources["milk"] -= item["milk"]


# create while loop to either sell drink or create report


while coffee_machine_on:
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if selection == "report":
        # prints report
        report()
    elif selection == "off":
        # turns the coffee machine off and break the while loop
        coffee_machine_on = False
    elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
        # check first if there are enough resources
        if check_resources(selection):
            # please insert coins
            print("Please insert coins.")
            quarters_in = int(input("How many quarters?: "))
            dimes_in = int(input("How many dimes?: "))
            nickels_in = int(input("How many nickels?: "))
            pennies_in = int(input("Hom many pennies?: "))
            item_price = MENU[f"{selection}"]["cost"]
            # sends info off to money_back to check if there's enough and get the change amount
            money_back = change(pennies_in, nickels_in, dimes_in, quarters_in, item_price)
            # function return -1 if the user didn't insert enough coins
            if money_back != -1:
                # since we have the ingredients and enough money, deduct from the resources
                deduct_resources(selection)
                if money_back == 0:
                    # it never hurts to be polite
                    print("Thank you for the exact change.")
                else:
                    # returns the change rounded to 2 decimal places
                    change_returned = round(money_back, 2)
                    print(f"Here is ${change_returned} in change.")

                # this is just good customer service here
                print(F"Here is your {selection}. Enjoy!")

                # add to the piggy bank
                money += item_price
            else:
                # go away you cheapskate
                print("Sorry that's not enough money. Money refunded")

    else:
        # in case you're like me and entered "cappucino" and had the program crash - this is for you
        print("Please try again.")
