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


def isBinary(node):
    if node:
        children = []
        root = node.root
        hold = {'current': root.value, 'lower_bound':-999999 , 'upper_bound': 9999999}
        children.append(hold)
        while len(children):
            children.remove(hold)
            if not hold['lower_bound'] <= hold['current'] <= hold['upper_bound']:
                return False
            elif root.left:
                children.append(root.left)
            elif root.right:
                children.append(root.right)
    return True

# Alternative solution
def check_tree(root, _min, _max):
    if root == None:
        return 1
    if _min > root.val  or root.val > _max:
        return 0
    return check_tree(root.left_ptr, _min, root.val) and check_tree(root.right_ptr, root.val, _max)

def isBST(root):
    _min = float('-inf')
    _max = float('inf')
    return check_tree(root, _min, _max)


