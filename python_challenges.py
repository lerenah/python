class Linked_List:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.down = None

  def get_next(self):
    return self.next

  def set_next(self, node):
    self.next = node

  def has_next(self):
    if self.next != None:
      return True
    else:
      return False

  def get_down(self):
    return self.down

  def set_down(self, node):
    self.down = node

  def has_down(self):
    if self.down != None:
      return True
    else:
      return False

node_values = [1,2,3,4,5,6,7,8,9,10]
node_list = []

for val in node_values:
  node_list.append(Linked_List(val))


def flatten(node):
  current = node
  end_node = node
  while current != None:
    if current.has_down():
      last_down = flatten(current.down)
      last_down.set_next(current.get_next())
      current.set_next(current.get_down())
      current.set_down(None)
    end_node = current
    current = current.next
  return end_node

''' ******************************************************************* '''
def circle_of_kids(n, m):
    last_kid = 0
    count = 0
    start = 0
    kids = []
    for i in range(1, n + 1):
        kids.append(i)

    while count <= m and len(kids) > 1:
        count += 1
        if count == m:
            if count <= len(kids):
                kids.remove(kids[count - 1])
                start = count - 1
            else:
                start = m - (len(kids) + 1)
                kids.remove(kids[start])
            if start < len(kids):
                last_kid = kids[start]
                kids = kids[start:] + kids[:start]
            count = 0

    return last_kid



'''
Get Safe Neighbors Function
'''
matrix = [
    [1, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 0]
]

'''
result:
[
    [2, 5, 2, 0],
    [0, 3, 0, 1],
    [3, 6, 4, 4],
    [0, 4, 2, 0]
]
'''
def get_near_neighbors(row, col, web):
    friends = 0

    copy_col = col
    # walk to the left
    while copy_col >= 0:
        if (copy_col - 1) >= 0:
            if web[row][copy_col - 1] == 0:
                break
            elif web[row][copy_col - 1] == 1:
                friends += 1
        copy_col -= 1

    # walk to the right
    copy_col = col
    while (copy_col + 1) in range(len(web)):
        if copy_col < len(web):
            if web[row][copy_col + 1] == 0:
                break
            elif web[row][copy_col + 1] == 1:
                friends += 1
        copy_col += 1

    # walk up
    copy_row = row
    while copy_row >= 0:
        if (copy_row - 1) >= 0:
            if web[copy_row - 1][col] == 0:
                break
            elif web[copy_row - 1][col] == 1:
                friends += 1
        copy_row -= 1

    # walk down
    copy_row = row
    while (copy_row + 1) in range(len(web)):
        if copy_row < len(web):
            if web[copy_row + 1][col] == 0:
                break
            elif web[copy_row + 1][col] == 1:
                friends += 1
        copy_row += 1

    return friends


'''
Solves MineSweeper game!
'''
def safe_steps(web):
    for idx, val in enumerate(web):
        for index, el in enumerate(val):
            if el != 0:
                web[idx][index] = get_near_neighbors(idx, index, web)
    return web

print(safe_steps(matrix))

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

'''
Working with Robot Classes
'''
import random

class Robot:
    def __init__(self):
        self.d_floor = 0
        self.d_jumps = 0
        self.random = random.randint(0, 2) * 1

    def unreliableJump(self):
        if self.random == 1:
            self.d_floor += 1
            self.d_jumps += 1
            return True
        else:
            return False

    def reliableJump(self):
        self.random = 1
        self.unreliableJump()


'''
Stock Price Class
'''

class StockPrices:

    def __init__(self):
        self.stocks = []

    def addPrice(self, stock, price):
        counter = 0
        if price <= 0:
            return 'Price must be a positive integer.'

        while counter < len(self.stocks):
            if stock == self.stocks[counter]['name']:
                self.stocks[counter]['price'].append(price)
                return
            counter += 1

        self.stocks.append({'name': stock, 'price': [price]})

    def getPrices(self, stock, n):
        if n <= 0:
            return 'The number of prices requested must be a positive integer.'
        for el in self.stocks:
            if stock == el['name']:
                total_stocks = len(el['price'])
                if n in range(total_stocks):
                    return el['price'][:n]
                elif n > len(el['price']):
                    return el['price']
            else:
                continue

        else:
            return 'This stock is not yet in our listing.'









