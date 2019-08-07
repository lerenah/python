class Solution:
  def levelOrder(self, root: TreeNode) -> List[List[int]]:
      from collections import deque
      result = []
      if root is None:
          return result
      q = deque()
      q.append(root)
      while q:
          level = len(q)
          curr_level = []
          for _ in range(level):
              node = q.popleft()
              curr_level.append(node.val)
              if node.left:
                  q.append(node.left)
              if node.right:
                  q.append(node.right)
          result.append(curr_level)

      return result
