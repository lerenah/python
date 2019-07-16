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
        self.visited = []

    def dfs(self, root, row=0, col=0):
        if root.left:
            self.dfs(root.left, row + 1, col - 1)
        self.visited.append((root.data, row, col))
        if root.right:
            self.dfs(root.right, row + 1, col + 1)

    def decode(self):
        self.visited.sort(key=lambda x: (x[2], x[1]))
        for el in self.visited:
            self.code += el[0]
        return self.code

    def print_tree(self, node):
        print(node.data, '/\n')
        if node.left:
            self.print_tree(node.left)
        if node.right:
            self.print_tree(node.right)
