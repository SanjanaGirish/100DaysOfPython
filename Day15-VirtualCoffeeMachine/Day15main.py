# Desired Output:
# https://replit.com/@appbrewery/coffee-machine-final?embed=1&output=1#main.py

import menu
machine = "on"
Water = 300
Milk = 200
Coffee = 100
Money = 0


def coin_machine():
    global total
    print("Please insert coins.")
    quarters = int(input("how many quarters?:")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.1
    nickels = int(input("how many nickles?:")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total = quarters + dimes + nickels + pennies


def check_change(cost, tot, drink):
    if cost > tot:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = tot - cost
        print(f"Here is {change} in change.")
        print(f"Here is your {drink} ☕️. Enjoy!")
        return True

while machine == "on":
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == 'report':
        print(f"Water: {Water}ml\nMilk: {Milk}ml\nCoffee: {Coffee}\n"
              f"Money: ${Money}")
    if choice == 'off':
        machine = "off"
    if choice == 'espresso':
        if Water < 50:
            print("Sorry there is not enough water.")
        elif Coffee < 18:
            print("Sorry there is not enough coffee.")
        else:
            coin_machine()
            if check_change(1.5, total, 'espresso'):
                Water -= 50
                Coffee -= 18
    elif choice == 'latte':
        if Water < 200:
            print("Sorry there is not enough water.")
        elif Coffee < 24:
            print("Sorry there is not enough coffee.")
        elif Milk < 150:
            print("Sorry there is not enough milk.")
        else:
            coin_machine()
            if check_change(2.5, total, 'latte'):
                Water -= 200
                Coffee -= 24
                Milk -= 150
    elif choice == 'cappuccino':
        if Water < 250:
            print("Sorry there is not enough water.")
        elif Coffee < 24:
            print("Sorry there is not enough coffee.")
        elif Milk < 100:
            print("Sorry there is not enough milk.")
        else:
            coin_machine()
            if check_change(3.0, total, 'cappuccino'):
                Water -= 250
                Milk -= 100
                Coffee -= 24





