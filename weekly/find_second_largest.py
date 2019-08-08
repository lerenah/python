def find_second_largest(root_node):

  # Find the second largest item in the binary search tree
  nodes = []

  in_order_traversal(nodes, root_node)

  return nodes[-2]

def in_order_traversal(arr, node):
  if node is None:
      return
  in_order_traversal(arr, node.left)
  arr.append(node.value)
  in_order_traversal(arr, node.right)
