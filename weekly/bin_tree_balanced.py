# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



#better solution
def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    self.diff = 0
    def helper(node):
        if not node:
            return 0
        left = helper(node.left)
        right = helper(node.right)
        self.diff = max(self.diff, abs(left-right))
        return 1 + max(left,right)

    helper(root)
    return False if self.diff > 1 else True 



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
