class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        from collections import deque

        if root is None:
            return
        q = deque()
        q.append(root)
        while q:
            length = len(q)
            if length > 1:
                i = 0
                while i + 1 in range(len(q)):
                    q[i].next = q[i + 1]
                    i += 1
            for _ in range(length):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root
