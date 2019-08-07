class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        from collections import deque
        result = []
        if root is None:
            return result
        q = deque()
        q.append(root)
        while q:
            level = len(q)
            averages = 0
            for _ in range(level):
                node = q.popleft()
                averages += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(averages / level)

        return result


# class Solution:
#   def averageOfLevels(self, root: TreeNode) -> List[float]:
#       from collections import deque
#       import numpy as np
#       result = []
#       if root is None:
#           return result
#       q = deque()
#       q.append(root)
#       while q:
#           level = len(q)
#           averages = []
#           for _ in range(level):
#               node = q.popleft()
#               averages.append(node.val)
#               if node.left:
#                   q.append(node.left)
#               if node.right:
#                   q.append(node.right)
#           result.append(np.mean(averages))

#       return result
