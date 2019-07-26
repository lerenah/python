class Node:
    def __init__(self, value):
        self.value = value
        self.children = []



class Tree:
    def __init__(self, node):
        self.root = node
        self.sums = []

    def dfs(self, node, total=[]):
        if len(node.children) == 0:
            total.append(node.value)
            self.sums.append(sum(total))
            total = []
            return
        q = []
        q.append(node)
        while len(q):
            parent = q.pop()
            total.append(parent.value)
            if len(parent.children):
                for el in parent.children:
                    self.dfs(el, total)
                    total.pop()

    def get_sales_path(self):
        return min(self.sums)
