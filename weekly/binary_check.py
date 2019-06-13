class BinaryTree:

    def __init__(self, node):
        self.root = node
        self.left = None
        self.right = None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def insert_right(self,node):
        if self.right is None:
            self.right = BinaryTree(node)

        else:
            newNode = BinaryTree(node)
            newNode.right = self.right
            self.right = newNode

    def insert_left(self, node):
        if self.left is None:
            self.left = BinaryTree(node)

        else:
            newNode = BinaryTree(node)
            newNode.left = self.left
            self.left = newNode

    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        if self.right is not None:
            self.right.print_tree()
        print(self.root)


def binary_check(node):
    if node:
        children = []
        root = node.root
        while node.left:
            children.append(node.get_left().root)
            print(node.get_left().root)
            node = node.left
        maxed = max(children)
        if root < maxed:
            return False
