import random
import sqlite3

bank_dict = {}
balance = 0


def luhn(n, check=False):
    num_lst = list(map(int, str(n)))
    last_num = num_lst.pop()
    num_lst = [j if i % 2 != 0 else j * 2 for i, j in enumerate(num_lst)]
    num_lst = [j - 9 if j > 9 else j for i, j in enumerate(num_lst)]
    if check:
        return bool((last_num + sum(num_lst)) % 10 == 0)
    return sum(num_lst)


def num_required_to_make_divisible_by_10(control_num):
    for i in range(10):
        if control_num % 10 == 0:
            return control_num
        control_num += 1


def ccnum_gen():
    num = int('400000' + str(random.randint(0, 999999999)).zfill(10))
    control_num = luhn(num)
    checksum = num_required_to_make_divisible_by_10(control_num) - control_num
    ccnum = str(num)[:-1] + str(checksum)
    return ccnum


try:
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    cur.execute('create table card (id INTEGER, number TEXT, pin TEXT,balance INTEGER DEFAULT 0);')
except:
    pass

id = 1

try:
    while True:
        user_choice = int(input("1. Create an account\n2. Log into account\n0. Exit\n"))
        if user_choice == 0:
            break
        elif user_choice == 1:
            print("\nYour card has been created")
            card_no = ccnum_gen()
            pin = str(random.randint(0000, 9999)).zfill(4).strip()
            bank_dict[card_no] = pin
            print(f"Your card number:\n{card_no}")
            print(f"Your card PIN:\n{pin}\n")
            cur.execute(f'insert into card values ({id}, {card_no}, {pin}, {balance});')
            id += 1
            conn.commit()
        elif user_choice == 2:
            card_no = input("\nEnter your card number:\n").strip()
            pin = input("Enter your PIN:\n").strip()
            if card_no not in bank_dict or bank_dict[card_no] != pin:
                print("\nWrong card number or PIN!\n")
            else:
                print("\nYou have successfully logged in!\n")
                while True:
                    print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
                    choice = int(input())
                    if choice == 1:
                        balance = cur.execute(f'select balance from card where number={card_no};')
                        print(f"\nBalance: {balance.fetchone()[0]}\n")
                        conn.commit()
                    elif choice == 2:
                        income = int(input("\nEnter income:\n"))
                        cur.execute(f'update card set balance=balance+{income} where number={card_no}')
                        conn.commit()
                        print("Income was added!\n")
                    elif choice == 3:
                        transfer_card_no = input("Transfer\nEnter card number:\n")
                        balance = cur.execute(f'select balance from card where number={card_no};').fetchone()[0]
                        if card_no == transfer_card_no:
                            print("You can't transfer money to the same account!\n")
                            continue
                        if not luhn(transfer_card_no, True):
                            print("Probably you made mistake in the card number. Please try again!\n")
                            continue
                        if not cur.execute(f'select number from card where number={transfer_card_no}').fetchall():
                            print("Such a card does not exist.")
                            continue
                        transfer_amt = int(input("Enter how much money you want to transfer:\n"))
                        if transfer_amt > balance:
                            print("Not enough money!")
                            continue
                        else:
                            cur.execute(f'update card set balance = balance-{transfer_amt} where number = {card_no}')
                            cur.execute(f'update card set balance = balance+{transfer_amt} where number = {transfer_card_no}')
                            print("Success!")
                            conn.commit()
                    elif choice == 4:
                        cur.execute(f'delete from card where number={card_no}')
                        print("The account has been closed!")
                        conn.commit()
                    elif choice == 5:
                        print("\nYou have successfully logged out!\n")
                        break
                    elif choice == 0:
                        break
    print("\nBye!")
except:
    pass