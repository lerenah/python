class ConnectFour:
    def __init__(self, m):
        self.board = []
        self.make_board(m)
        self.player1 = 'R'
        self.player2 = 'Y'
        self.col = 0
        self.col_fill = {}
        self.max_length = 0

    def make_board(self, m):
        for i in range(m):
            col = []
            self.board.append(col)
        print(self.board)

    def move(self, player, col):
        col -= 1
        if player == 1:
            self.board[col].append(self.player1)
            if len(self.board[col]) > self.max_length:
                self.max_length = len(self.board[col])
            if col not in self.col_fill:
                self.col_fill[col] = [self.player1]
            else:
                self.col_fill[col].append(self.player1)
        else:
            self.board[col].append(self.player2)
            if len(self.board[col]) > self.max_length:
                self.max_length = len(self.board[col])
            if col not in self.col_fill:
                self.col_fill[col] = [self.player2]
            else:
                self.col_fill[col].append(self.player2)

        print(self.board)



    def scoring_op(self, chip):
        for idx, col in enumerate(self.board):
            col.append(chip)
            count = 0
            # check vertical
            for el in col:
                if el == chip:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    col.pop()
                    return f'Column {idx + 1} has a scoring opportunity for {chip}!'
            col.pop()

        # check horizontal
        changes = {}
        for id, col in enumerate(self.board):
            col.append(chip)
            changes[id] = len(col) - 1
        idx = 0
        j = 0
        while j in range(self.max_length):
            while idx in range(len(self.board)):
                if self.board[idx][j] == chip and idx + 3 in range(len(self.board)):
                    if self.board[idx + 1][j] == chip and self.board[idx + 2][j] == chip and self.board[idx + 3][j] == chip:
                        column = 0
                        for key, val in changes.items():
                            if val == j:
                                column = key
                        for col in self.board:
                            col.pop()
                        return f'Column {column + 1} has a scoring opportunity for {chip}!'
                idx += 1
            j += 1

        # set the board back to the way it was
        for col in self.board:
            col.pop()

        return f'No current scoring opportunities for {chip} right now :('
