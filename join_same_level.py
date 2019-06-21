class BinNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinTree:
    def __init__(self, node):
        self.root = node

    def add_node(self, node):
        if self.root:
            curr = self.root
            if curr.value > node.value:
                if not curr.left:
                    curr.left = BinTree(node)
                else:
                    curr.left.add_node(node)
            elif curr.value < node.value:
                if not curr.right:
                    curr.right = BinTree(node)
                else:
                    curr.right.add_node(node)
        else:
            return "Value already in tree"

    def get_level(self, node):
        q = []
        q.append(node)
        while len(q):
            curr = q[0]
            q.remove(q[0])
            print(curr.root.value)
            if curr.root.left:
                curr.root.left.next = curr.root.right
                q.append(curr.root.left)
            if curr.root.right:
                if curr.root.left is not None:
                    if curr.root.left.next:
                        curr.root.right.next = curr.root.left.next.root.left
                q.append(curr.root.right)

