class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def print_tree(self, node):
        if not node.children:
            return
        if node.name:
            print(node.name)
            if len(node.children):
                node.children.sort(key=self.sort)
                for child in node.children:
                    print(child.name)
                    self.print_tree(child)


    def sort(self, child):
        return child.name
