class BinNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_left(self, data):
        self.left = BinNode(data)
        return self.left

    def add_right(self, data):
        self.right = BinNode(data)
        return self.right


class BinTree:

    def __init__(self, node=None):
        self.root = node
        self.message = []
        self.code = ''

    def bfs(self, node):
        q = [node]
        root = q.pop(0)
        if root.left:
            self.bfs(root.left)
        self.message.append(root.data)
        if root.right:
            self.message.append('|')
            self.bfs(root.right)

    def decode(self):
        idx = self.message.index('|')
        left_side = self.message[:idx]
        right_side = self.message[idx + 1:]
        if len(left_side) >= len(right_side):
            starter_arr = left_side
            non_starter = right_side
        else:
            starter_arr = right_side
            non_starter = left_side
        i = 0
        while i < len(starter_arr) and i in range(len(non_starter)):
            self.code += starter_arr[i]
            self.code += non_starter[i]
            i += 1
            print(self.code)
        if len(starter_arr):
            self.code += ''.join(starter_arr[i:])
        return self.code

    def print_tree(self, node):
        print(node.data, '/\n')
        if node.left:
            self.print_tree(node.left)
        if node.right:
            self.print_tree(node.right)
