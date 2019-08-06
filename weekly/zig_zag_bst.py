from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  # TODO: Write your code here
  if root is None:
    return result
  q = deque()
  q.append(root)
  next_level = True
  while q:
    l = len(q)
    level = []
    for _ in range(l):
      node = q.popleft()
      level.append(node)
      if not next_level:
        if node.left:
            q.appendleft(node.left)
        if node.right:
          q.appendleft(node.right)
      else:
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
    result.append(level)
    next_level = not next_level

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()
