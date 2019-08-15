def inorderSuccessor(self, node):
  """
  :type node: Node
  :rtype: Node
  """
  if node is None:
      return node

  def find_min(root):
      while root.left:
          root = root.left
      return root

  curr = node
  if curr.right is not None:
      successor = find_min(curr.right)
      return successor
  else:
      ancestor = curr.parent
      successor = None
      if ancestor and ancestor.val < curr.val:
          while ancestor and ancestor.val < curr.val:
              successor = ancestor
              ancestor = ancestor.parent

      return ancestor
