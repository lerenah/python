class Binary_Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class Binary_Tree:
  def __init__(self, root):
    self.root = Binary_Node(root)

  def add_node(self, value):
    if self.root is None:
      self.root = Binary_Node(value)
    else:
      node = self.root
      if value < node.value:
        if not node.left:
          node.left = Binary_Node(value)
        else:
          self.add_node(node.left)
      elif value > node.value:
        if not node.right:
          node.right = Binary_Node(value)
        else:
          self.add_node(node.right)

  def preorder_traversal(self, node):
    if node:
      print(str(node.value) + '<-->')
      self.preorder_traversal(node.left)
      self.preorder_traversal(node.right)


  def postorder_traversal(self, node):
    if node:
      self.postorder_traversal(node.left)
      self.postorder_traversal(node.right)
      print(str(node.value) + '<-->')

  def inorder_traversal(self, node):
    if node:
      self.inorder_traversal(node.left)
      print(str(node.value) + '<-->')
      self.inorder_traversal(node.right)
