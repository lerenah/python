class BinNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def set_value(self,val):
        self.val = val

    def get_value(self):
        return self.val

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right !=None

    def __repr__(self):
        return f'Node({self.get_value()}'

class Tree:
    def __init(self, val):
        self.root = BinNode(val)

    def get_root(self):
        return self.root

    def set_root(self,val):
        self.root = BinNode(val)

    def compare(self, node, new_node):
        if new_node.get_val() == node.get_val():
            return 0
        elif new_node.get_val() < node.get_val():
            return -1
        else:
            return 1
