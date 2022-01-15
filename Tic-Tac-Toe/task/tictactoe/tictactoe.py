def print_ttt(ttt='         '):
    print('---------')
    for i in range(0, len(ttt), 3):
        print(f'| {ttt[i]} {ttt[i + 1]} {ttt[i + 2]} |', end=" ")
        print()
    print('---------')


def ask_user_input():
    global ttt
    global count
    ttt_dict = {
        (1, 1): 6,
        (1, 2): 3,
        (1, 3): 0,
        (2, 1): 7,
        (2, 2): 4,
        (2, 3): 1,
        (3, 1): 8,
        (3, 2): 5,
        (3, 3): 2
    }

    try:
        x, y = map(int, input("Enter the coordinates: ").split())
    except ValueError:
        print("You should enter numbers!")
        ask_user_input()

    if not (1 <= x <= 3) or not (1 <= y <= 3):
        print("Coordinates should be from 1 to 3!")
        ask_user_input()

    elif ttt[ttt_dict[(x, y)]] in ['X', 'O']:
        print("This cell is occupied! Choose another one!")
        ask_user_input()
    else:
        l = 'X' if count % 2 == 0 else 'O'
        ttt[ttt_dict[(x, y)]] = l
        print_ttt(ttt)
        count += 1
        return ttt, count


def check_state(ttt):
    state = set()

    win = ['036', '147', '258', '012', '345', '678', '048', '246']
    for i in win:
        i1, i2, i3 = list(map(int, i))
        if ttt[i1] == 'X' and ttt[i2] == 'X' and ttt[i3] == 'X':
            state.add('X wins')
        if ttt[i1] == 'O' and ttt[i2] == 'O' and ttt[i3] == 'O':
            state.add('O wins')

    if len(state) > 1 or ttt.count('X') - ttt.count('O') >= 2 or ttt.count(
            'O') - ttt.count('X') >= 2:
        return 'Impossible'
    elif len(state) == 1:
        return str(list(state)[0])
    elif ' ' not in ttt:
        return 'Draw'
    else:
        return 'Game not finished'


count = 0
ttt = list('         ')
print_ttt()

while True:
    ask_user_input()
    if check_state(ttt) in ['X wins', 'O wins', 'Draw']:
        break
print(check_state(ttt))
