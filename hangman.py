import random

def hangman(word):
    wrong = 0
    stages = ['',
              '            ',
              '______      ',
              '|           ',
              '|    |      ',
              '|    o      ',
              '|  / | \    ',
              '|  /   \    ',
              '|           ',
              ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Welcom to hangman!')
    while wrong < len(stages) -1:
        print(board)
        print('\n')
        msg = 'Guess a character'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print('\n'.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('You win!')
            print('_'.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print('You lose! The answer is .{}.'.format(word))

answers = ['cat','dog','mouse','hourse','mokey']
num = random.randint(0,len(answers)-1)
hangman(answers[num])

