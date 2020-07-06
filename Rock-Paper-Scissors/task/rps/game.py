import random

file = open('rating.txt')
rating_dict = {}

for line in file.readlines():
    k, v = line.split()
    rating_dict[k] = int(v)

file.close()


def b_beats_a(a, b):
    x = options_list.index(a)
    y = options_list.index(b)
    l = len(options_list) // 2
    return x < y and y - x <= l or y < x and x - y > l


def rps(user_choice, computer_choice):
    if computer_choice == user_choice:
        print(f"There is a draw ({computer_choice})")
        rating_dict[user_name] += 50
    elif b_beats_a(user_choice, computer_choice):
        print(f"Sorry, but computer chose {computer_choice}")
    else:
        print(f"Well done. Computer chose {computer_choice} and failed")
        rating_dict[user_name] += 100


user_name = input("Enter your name: ")
print(f"Hello, {user_name}")
options_list = list(input().split(','))
if options_list == ['']:
    options_list = ['rock', 'paper', 'scissors']
print("Okay, let's start")
rating_dict.setdefault(user_name, 0)

while True:
    computer_choice = random.choice(options_list)
    user_choice = input()

    if user_choice in options_list:
        rps(user_choice, computer_choice)
    elif user_choice == '!exit':
        print("Bye!")
        break
    elif user_choice == '!rating':
        print(f"Your rating: {rating_dict.setdefault(user_name, 0)}")
    else:
        print("Invalid input")
