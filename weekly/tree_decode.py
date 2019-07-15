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
        self.left_counts = 0
        self.right_counts = 0
        self.peak = []
        self.code = ''

    def get_most_left(self, node, count=0):
        if node.left:
            count += 1
            self.get_most_left(node.left, count)
            self.message.append((node.left.data, count))
        print(node.data, 'is current node')
        if node.right:
            self.right_counts += 1
            self.get_most_left(node.right)

    def get_leftest(self):
        maximum = max(sorted(self.message, key=lambda s: s[1]))
        print(maximum[0])
        self.code += maximum[0]
        print(self.message)

    def bfs(self, node):
        q = [node]
        self.peak.append(node.data)
        while len(q):
            root = q.pop(0)
            print(root.data)
            if root.left:
                q.append(root.left)
                print(self.code)
                self.message.append(root.left.data)
            # print(self.message)
            if root.right:
                q.append(root.right)
                self.message.append(root.right.data)
        print(self.peak)
        print(self.message)

    def decode(self):
        self.code += self.message.pop()
        self.code += self.message.pop(0)
        self.code += self.message.pop()
        self.code += self.peak.pop(0)
        self.code += self.message.pop()
        self.code += self.peak.pop()

        print(self.code)

    def print_tree(self, node):
        print(node.data, '/\n')
        if node.left:
            self.print_tree(node.left)
        if node.right:
            self.print_tree(node.right)
