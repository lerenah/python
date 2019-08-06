class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        q = []
        count = 1
        next_level = (count * 2) + 1
        if root:
            q.append(root)
            while len(q):
                if len(q) > 1:
                    if count == next_level:
                        q[0].next = None
                        next_level = (count * 2) + 1
                    else:
                        q[0].next = q[1]
                node = q.pop(0)
                count += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root
