import random
from string import ascii_lowercase

word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)


def index(word):
    d = {}
    for i, j in enumerate(word):
        if j in d:
            d[j] += [i]
        else:
            d[j] = [i]
    return d


def hyphen(word_lst, letter, pos_lst):
    for i in pos_lst:
        word_lst[i] = letter
    return word_lst


def hyphenator(word, letters_set):
    word_lst = list('-' * len(word))
    pos_lst = index(word)
    for i in letters_set:
        word_lst = hyphen(word_lst, i, pos_lst[i])
    return "".join(word_lst)


def play_hangman():
    letters_set = set()
    typed_letters = set()
    count = 8

    while True:
        hword = hyphenator(word, letters_set)
        print(hword)

        if '-' not in hword:
            print("You guessed the word!")
            print("You survived!")
            break

        letter = input("Input a letter: ")

        if len(letter) != 1:
            print("You should input a single letter\n")
            continue

        if letter not in ascii_lowercase:
            print("It is not an ASCII lowercase letter\n")
            continue

        if letter in typed_letters:
            print("You already typed this letter\n")
            continue
        typed_letters.add(letter)

        if letter in word:
            letters_set.add(letter)
        else:
            print("No such letter in the word")
            count -= 1

        if count <= 0:
            print("You are hanged!")
            break
        print()


print('H A N G M A N\n')
while True:
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == 'play':
        play_hangman()
    else:
        exit()
