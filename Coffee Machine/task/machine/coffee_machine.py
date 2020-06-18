water, milk, coffee_beans, no_of_cups, money = 400, 540, 120, 9, 550


def print_coffee_machine_status():
    print(f"""The coffee machine has:
    {water} of water
    {milk} of milk
    {coffee_beans} of coffee beans
    {no_of_cups} of disposable cups
    ${money} of money""")

def check_status(buy_option):
    global water,milk,coffee_beans,money,no_of_cups

    if buy_option == 'back':
        return

    elif buy_option == 1:
        if water<250:
            print("Sorry, not enough water!")
        elif coffee_beans<16:
            print("Sorry, not enough coffee beans!")
        else:
            water -= 250
            coffee_beans -= 16
            money += 4
            print('I have enough resources, making you a coffee!')
            no_of_cups -= 1

    elif buy_option == 2:
        if water<350:
            print("Sorry, not enough water!")
        elif milk<75:
            print("Sorry, not enough milk!")
        elif coffee_beans<20:
            print("Sorry, not enough coffee beans!")
        else:
            water -= 350
            milk -= 75
            coffee_beans -= 20
            money += 7
            print('I have enough resources, making you a coffee!')
            no_of_cups -= 1


    elif buy_option == 3:
        if water<200:
            print("Sorry, not enough water!")
        elif milk<100:
            print("Sorry, not enough milk!")
        elif coffee_beans<12:
            print("Sorry, not enough coffee beans!")
        else:
            water -= 200
            milk -= 100
            coffee_beans -= 12
            money += 6
            print('I have enough resources, making you a coffee!')
            no_of_cups -= 1

while True:
    user_input = input("Write action (buy, fill, take, remaining, exit):\n")

    if user_input == 'buy':
        buy_option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if buy_option == 'back':
            continue
        else:
            check_status(int(buy_option))


    elif user_input == 'fill':
        fill_water = int(input("Write how many ml of water do you want to add:\n"))
        fill_milk = int(input("Write how many ml of milk do you want to add:\n"))
        fill_coffee_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
        fill_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))

        water += fill_water
        milk += fill_milk
        coffee_beans += fill_coffee_beans
        no_of_cups += fill_cups
        
    elif user_input == 'take':
        print(f"I gave you ${money}")
        money = 0
        
    elif user_input == 'remaining':
        print_coffee_machine_status()
            
    elif user_input == 'exit':
        exit()