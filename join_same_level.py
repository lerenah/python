class BinNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_right(self, node):
        return node.right

    def get_left(self, node):
        return node.left

    def set_next(self, node):
        self.next = node


def print_nodes(node):
    if node:
        if node.left:
            print_nodes(node.left)
        print(node.value)
        if node.right:
            print_nodes(node.right)


def breadth_print(node):
    if node:
        q = []
        q.append(node)
        while len(q):
            curr = q.pop(0)
            if curr.left:
                q.append(curr.left)
                breadth_print(curr.left)
            # print(curr.value)
            if curr.right:
                q.append(curr.right)
                breadth_print(curr.right)
            if len(q) == 2:
                q[0].set_next(q[1])
                print(q[0].value, q[0].next.value)
                q = []
