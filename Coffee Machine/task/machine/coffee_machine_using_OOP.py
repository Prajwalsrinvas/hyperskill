class Coffee:

    # Class attributes
    READY_COFFEE = "I have enough resources, making you a coffee!"
    WATER_ERROR = "Sorry, not enough water!"
    MILK_ERROR = "Sorry, not enough milk!"
    BEAN_ERROR = "Sorry, not enough Coffee beans!"

    # Constructor to invoke initial state of the coffee machine
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    # print the state of coffee machine
    def print_data(self):
        print(f"""The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.beans} of coffee beans
        {self.cups} of disposable cups
        ${self.money} of money""")

    # Buy coffee
    def buy_coffee(self, option):
        if option == '1':  # espresso
            if self.water < 250:
                print(Coffee.WATER_ERROR)
            elif self.beans < 16:
                print(Coffee.BEAN_ERROR)
            else:
                print(Coffee.READY_COFFEE)
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
        elif option == '2':  # latte
            if self.water < 350:
                print(Coffee.WATER_ERROR)
            elif self.beans < 20:
                print(Coffee.BEAN_ERROR)
            elif self.milk < 75:
                print(Coffee.MILK_ERROR)
            else:
                print(Coffee.READY_COFFEE)
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
        elif option == '3':  #cappuccino
            if self.water < 200:
                print(Coffee.WATER_ERROR)
            elif self.beans < 12:
                print(Coffee.BEAN_ERROR)
            elif self.milk < 100:
                print(Coffee.MILK_ERROR)
            else:
                print(Coffee.READY_COFFEE)
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1

    # Add ingredients
    def fill_coffee(self, water_quantity, milk_quantity, bean_quantity, disp_cups):
        self.water += water_quantity
        self.milk += milk_quantity
        self.beans += bean_quantity
        self.cups += disp_cups

    # Take money
    def take_money(self):
        print(f"I gave you {self.money}")
        self.money = 0


# Initialize the coffee machine
coffee = Coffee(400, 540, 120, 9, 550)

def initiate_action(input_action):
    if input_action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        buy_option = input()
        if buy_option != 'back':
            coffee.buy_coffee(buy_option)
    elif input_action == "fill":
        print("Write how many ml of water do you want to add:")
        add_water = int(input())
        print("Write how many ml of milk do you want to add:")
        add_milk = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        add_beans = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        add_disp_cups = int(input())
        coffee.fill_coffee(add_water, add_milk, add_beans, add_disp_cups)
    elif input_action == 'take':
        coffee.take_money()
    elif input_action == 'remaining':
        print("remaining executing!")
        coffee.print_data()

while True:
    print("Write action (buy, fill, take, remaining, exit):")
    input_action = input()
    if input_action == 'exit':
        break
    else:
        initiate_action(input_action)
