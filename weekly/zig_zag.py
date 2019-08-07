class Solution:
  def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
      if root is None:
          return []
      result = []
      from collections import deque

      q = deque()
      q.append(root)
      zig_zag = True

      while q:
          level = len(q)
          curr_level = deque()

          for _ in range(level):
              node = q.popleft()
              if zig_zag:
                  curr_level.append(node.val)
              else:
                  curr_level.appendleft(node.val)
              if node.left:
                  q.append(node.left)
              if node.right:
                  q.append(node.right)

          zig_zag = not zig_zag
          result.append(curr_level)

      return result
