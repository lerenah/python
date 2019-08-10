def find_successor(root, key):
  # TODO: Write your code here
  result = 0
  q = deque()
  q.append(root)
  while q:
    level = []
    for _ in range(len(q)):
      node = q.popleft()
      level.append(node)
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
      if node.val == key:
        return q.popleft()

  return None
