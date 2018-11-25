
def render(board, takenRow=None):
    table = ''

    for i in range(len(board)):
        if not board[i]:
            table += '.'
        else:
            if takenRow and i in takenRow:
                table += '\x1b[33m' + board[i] + '\x1b[0m'
            else:
                table += board[i]

        table += ' '

        if i%3 == 2:
            table += '\n'
    
    print(table)


class TicTacToe:

    def __init__(self):
        self.player = 'X'
        self.utility = 0
        self.board = ['' for i in range(9)]

    def actions(self):
        return [ i for i, el in enumerate(self.board) if el == '' ]

    def isTerminal(self):
        return self.utility != 0 or len(self.actions()) == 0
    
    def play(self, action):
        if action in self.actions():
            self.board[action] = self.player

            if self._3InRow(action):
                self.utility = 1 if self.player == 'X' else -1
            else:
                self.player = 'O' if self.player == 'X' else 'X'

    def _3InRow(self, action):
        rows = [ [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6] ]

        rows = filter(lambda row: action in row, rows)

        for row in rows:
            if (self.player == self.board[row[0]] and
                self.player == self.board[row[1]] and
                self.player == self.board[row[2]]):

                return row
        
        return None





import random
from colorama import init

init()

print('\nYou are X. In order to play type a number between 0 and 8.\n')
render(list(map(str, range(9))))
print('--------------START--------------\n')

game = TicTacToe()

render(game.board)


while not game.isTerminal():

    #print(game.player, ' : ', game.actions(), '\n')

    if (game.player == 'X'):
        action = int(input('> ')) 
    else:
        action = random.choice(game.actions())

    game.play(action)

    render(game.board, game._3InRow(action))


if (game.utility == 0):
    print('\x1b[33m', 'IT\'S A TIE', '\x1b[0m')
else:
    print('\x1b[33m', 'X' if game.utility == 1 else 'O', '\x1b[0m', 'WINS')
