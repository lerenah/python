'''
Tic Tac Toe Game
'''
class TicTacToe:
    def __init__(self):
        self.positions = {}
        self.moves = []
        self.board = []
        self.make_board()

    def make_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append((i,j))
            self.board.append(row)
        print(self.board)

    def access_move(self, n):
        for k in self.positions.keys():
            if k == self.moves[n - 1]:
                return 'The {}th move was an {} at {}'.format(n, self.positions[k], k)

    def record_move(self, value, pos):
        self.moves.append(pos)
        self.positions[pos] = value

    def make_move(self, value, pos):
        # update board
        self.board[pos[0]][pos[1]] = value
        # record move
        self.record_move(value, pos)
        print(self.board)

game1 = TicTacToe()
game1.make_move('X', (0,2))
