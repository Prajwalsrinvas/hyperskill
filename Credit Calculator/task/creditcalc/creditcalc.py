import argparse
import sys
from math import log, ceil

# argparse
parser = argparse.ArgumentParser()
parser.add_argument("--type", default=None)
parser.add_argument("--payment", default=0.0)
parser.add_argument("--principal", default=0.0)
parser.add_argument("--periods", default=0.0)
parser.add_argument("--interest", default=0.0)
args = parser.parse_args()

# take inputs from command line
type = args.type
monthly_payment = float(args.payment)
P = float(args.principal)
n = int(args.periods)
i = float(args.interest) / 100 / 12

# checking for less than 4 values and  negative numbers 
if len(sys.argv) - 1 < 4 or monthly_payment < 0 or P < 0 or n < 0 or i < 0:  # len - 1 as first value is path to file
    print("Incorrect parameters.")
    exit()

# calculate differentiated payments
if type == 'diff':
    def dm(m):
        return ceil((P / n) + i * (P - ((P * (m - 1)) / (n))))


    for j in range(1, n + 1):
        print(f"Month {j}: paid out {dm(j)}")
    op = int(sum([dm(j) for j in range(1, n + 1)]) - P)
    print(f"\nOverpayment = {op}")

# annuity payment
if type == 'annuity' and P and n and i:
    a = ceil((P) * ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
    op = int(n * a - P)
    print(f"Your annuity payment = {a}!")
    print(f"Overpayment = {op}")

# credit principal
if monthly_payment and n and i:
    P = (monthly_payment) / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
    op = ceil(n * monthly_payment - P)
    print(f"Your credit principal = {ceil(P)}!")
    print(f"Overpayment = {op}")

# how much time a user needs to repay the credit
elif P and monthly_payment and i:
    n = ceil(log((monthly_payment / (monthly_payment - i * P)), (i + 1)))
    y, m = ceil(n // 12), ceil(n % 12)
    yr = ''
    mn = ''
    a = ''
    yr, mn, a = f'{y} years', f'{m} months', 'and'
    if y == 1:
        yr = '1 year'
    if m == 1:
        mn = '1 month'
    if y == 0:
        yr, a = '', ''
    if m == 0:
        mn, a = '', ''
    print(f"You need {yr} {a} {mn} to repay this credit!")
    op = ceil(n * monthly_payment - P)
    print(f"Overpayment = {op}")
