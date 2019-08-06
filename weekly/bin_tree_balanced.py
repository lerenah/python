# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        counts = []

        def helper(root):
            left = 0
            right = 0
            if not root.left and not root.right:
                return 0
            if root.left:
                left += helper(root.left)
            if root.right:
                right += helper(root.right)
            print(left, ' is left')
            print(right, ' is right')
            num = 1 + max(left, right)
            counts.append(num)
            return num

        helper(root)
        i = 0
        while i + 1 in range(len(counts)):
            if counts[i] - counts[i + 1] > 1:
                return False
            i += 1
        return True
